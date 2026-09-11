#!/usr/bin/env python3
"""The module schedule: ONE file, module/schedule.json, that every view derives from.

The README's banner and schedule table, module/module-overview.md's topic
table, the site index and its redirect stubs, the labs page order, the
published schedule.json the Moodle course page reads, and the CI gate
(scripts/check_schedule.py) all import this module and read that file.
Nothing else in the repo may state a week number or a semester date.

Rows are consecutive calendar weeks; the "X" reading-week row is one of them,
so row i covers start + 7*i days. The start is DERIVED unless the file says
otherwise: reading week is always the week of the Irish October bank holiday
(the last Monday of October), so week 1 begins that many weeks earlier as
there are rows before the X row. A `startDate` (a Monday, YYYY-MM-DD) in the
file overrides the rule for a year that breaks it.

    from schedule import load
    sched = load()                       # this year's calendar
    for row in sched.rows: ...
    row = sched.row_for(datetime.date.today())   # None outside the semester
    sched.to_public()                    # builder-format dict, absolute URLs

The file is the same shape as an export from the lecturer's
module-schedule-table-builder app, minus the URLs: a row names its lecture and
lab by folder (`lecture`, `lab`), and an export's `lectureUrl`/`labUrl` are
accepted in their place.
"""
from __future__ import annotations

import datetime
import json
import re
from dataclasses import dataclass
from pathlib import Path

SCHEDULE = Path("module/schedule.json")
SITE = "https://danielcregg.is-a.dev/ai-assisted-programming/"
LECTURES = Path("lectures")
LABS = Path("labs")
MCQ = Path("mcq")
MCQ_RE = re.compile(r"^MCQ (\d)\b")
NAME_RE = re.compile(r"^[a-z0-9-]+$")


@dataclass(frozen=True)
class Row:
    index: int          # position in the semester, 0-based, reading week included
    week: str           # "1".."12", or "X" for the reading week
    topic: str          # "Coding Agents"; empty on MCQ and reading-week rows
    deck: str | None    # lectures/<deck>/slides.md
    lab: str | None     # labs/<lab>/
    assessment: str     # "PA3 (4%)", "MCQ 1 (32%)", or empty
    notes: str

    @property
    def is_break(self) -> bool:
        return self.week == "X"

    @property
    def mcq(self) -> str | None:
        """'1' for the MCQ 1 row, else None."""
        m = MCQ_RE.match(self.assessment)
        return m.group(1) if m else None

    @property
    def page(self) -> Path | None:
        """The non-teaching page an MCQ row owns: mcq/mcq<n>/README.md."""
        return MCQ / f"mcq{self.mcq}" / "README.md" if self.mcq else None

    @property
    def label(self) -> str:
        return self.topic or self.assessment or self.notes


@dataclass(frozen=True)
class Schedule:
    start: datetime.date
    derived: bool        # True when start came from the bank-holiday rule
    rows: tuple[Row, ...]
    raw: dict

    @property
    def reading_index(self) -> int:
        return next(r.index for r in self.rows if r.is_break)

    def monday(self, row: Row) -> datetime.date:
        return self.start + datetime.timedelta(weeks=row.index)

    def sunday(self, row: Row) -> datetime.date:
        return self.monday(row) + datetime.timedelta(days=6)

    @property
    def end(self) -> datetime.date:
        """The first Monday after the last row."""
        return self.start + datetime.timedelta(weeks=len(self.rows))

    def row_for(self, day: datetime.date) -> Row | None:
        i = (monday_of(day) - self.start).days // 7
        return self.rows[i] if 0 <= i < len(self.rows) else None

    @property
    def teaching(self) -> tuple[Row, ...]:
        return tuple(r for r in self.rows if r.deck)

    def deck_for_lab(self, lab: str) -> str | None:
        for r in self.rows:
            if r.lab == lab:
                return r.deck
        return None

    def to_public(self) -> dict:
        """The schedule as the site publishes it (build/schedule.json).

        Builder-format rows with absolute URLs, so the Moodle course page and
        the builder app can both read it; plus the resolved start and whether
        it was derived, so a reader can re-derive next year's dates itself.
        """
        weeks = []
        for r in self.rows:
            weeks.append({
                "week": r.week, "topic": r.topic,
                "lectureUrl": f"{SITE}{r.deck}/" if r.deck else "",
                "videoUrl": "", "notebookLmUrl": "",
                "labUrl": f"{SITE}labs/{r.lab}/" if r.lab else "",
                "assessment": r.assessment, "notes": r.notes,
            })
        extra = {k: v for k, v in self.raw.items()
                 if k not in ("weeks", "startDate", "_comment")}
        return {**extra, "startDate": self.start.isoformat(), "startDateDerived": self.derived,
                "readingWeekIndex": self.reading_index, "site": SITE, "weeks": weeks}


def monday_of(day: datetime.date) -> datetime.date:
    return day - datetime.timedelta(days=day.weekday())


def bank_holiday_monday(year: int) -> datetime.date:
    """The Irish October bank holiday: the last Monday of October."""
    return monday_of(datetime.date(year, 10, 31))


def _name(w: dict, key: str, url_key: str, prefix: str, week: str) -> str | None:
    """A folder name from `key`, or from a builder-export URL under `prefix`."""
    name = str(w.get(key, "") or "").strip()
    url = str(w.get(url_key, "") or "").strip()
    if not name and url:
        if not (url.startswith(prefix) and url.endswith("/")):
            raise SystemExit(f"schedule: week {week}: {url_key} must be {prefix}<name>/ (got {url!r})")
        name = url[len(prefix):].strip("/")
    if not name:
        return None
    if not NAME_RE.match(name):
        raise SystemExit(f"schedule: week {week}: {key} names {name!r}, which is not a "
                         f"kebab-case folder name")
    return name


def load(path: Path = SCHEDULE, year: int | None = None) -> Schedule:
    """Load the schedule; `year` picks which year's calendar (default: this one)."""
    if not path.is_file():
        raise SystemExit(f"schedule: {path} is missing. It is the module's only schedule.")
    raw = json.loads(path.read_text(encoding="utf-8"))
    rows = []
    for i, w in enumerate(raw.get("weeks", [])):
        week = str(w.get("week", "")).strip()
        rows.append(Row(
            index=i, week=week,
            topic=str(w.get("topic", "")).strip(),
            deck=_name(w, "lecture", "lectureUrl", SITE, week),
            lab=_name(w, "lab", "labUrl", SITE + "labs/", week),
            assessment=str(w.get("assessment", "")).strip(),
            notes=str(w.get("notes", "")).strip(),
        ))
    if not rows:
        raise SystemExit(f"schedule: {path} has no weeks")
    breaks = [r.index for r in rows if r.is_break]
    if len(breaks) != 1:
        raise SystemExit(f"schedule: {path} needs exactly one reading-week row (week \"X\"); found {len(breaks)}")

    if raw.get("startDate"):
        try:
            start = datetime.date.fromisoformat(str(raw["startDate"]))
        except ValueError:
            raise SystemExit(f"schedule: startDate must be YYYY-MM-DD (got {raw['startDate']!r})")
        derived = False
    else:
        if year is None:
            from zoneinfo import ZoneInfo
            year = datetime.datetime.now(ZoneInfo("Europe/Dublin")).year
        start = bank_holiday_monday(year) - datetime.timedelta(weeks=breaks[0])
        derived = True
    return Schedule(start=start, derived=derived, rows=tuple(rows), raw=raw)
