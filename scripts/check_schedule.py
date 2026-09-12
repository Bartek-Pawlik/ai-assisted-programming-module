#!/usr/bin/env python3
"""CI gate: module/schedule.json is the module's only schedule, and every view agrees.

Fails (exit 1, every finding listed) when:
  - the schedule itself is malformed: a startDate that is not a Monday, week
    numbers not 1..N in order, no lecture on a row that is neither an MCQ nor
    the reading week, a lecture row with no topic;
  - a row names a deck, lab or MCQ page that does not exist;
  - a folder under lectures/ or mcq/ is not claimed by any row (it would
    vanish from the site with CI green), or still carries a week number;
  - a deck declares `week:` in its frontmatter or a week number in its title
    kicker, or an MCQ page titles itself with a week -- the schedule is
    stated ONCE;
  - README's generated schedule table is stale (run update_current_week.py);
  - module/module-overview.md's topic table is missing a lecture topic or
    lists them out of schedule order.

Usage:
    python scripts/check_schedule.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from schedule import LABS, LECTURES, MCQ, load  # noqa: E402
import update_current_week  # noqa: E402

OVERVIEW = Path("module/module-overview.md")
README = Path("README.md")
TABLE_RE = re.compile(r"<!-- schedule-table:start -->\n(.*?)<!-- schedule-table:end -->", re.S)


def main() -> None:
    findings: list[str] = []
    sched = load()

    if sched.start.weekday() != 0:
        findings.append(f"start {sched.start} is a {sched.start:%A}, not a Monday")
    numbered = [r.week for r in sched.rows if not r.is_break]
    if numbered != [str(n) for n in range(1, len(numbered) + 1)]:
        findings.append(f"week numbers must run 1..N in order; got {numbered}")

    claimed_decks: set[str] = set()
    claimed_pages: set[str] = set()
    for r in sched.rows:
        if r.deck:
            claimed_decks.add(r.deck)
            if not (LECTURES / r.deck / "slides.md").is_file():
                findings.append(f"week {r.week}: lectures/{r.deck}/slides.md does not exist")
            if not r.topic:
                findings.append(f"week {r.week}: a lecture row needs a topic")
        elif r.mcq:
            claimed_pages.add(f"mcq{r.mcq}")
            if not r.page.is_file():
                findings.append(f"week {r.week}: {r.page.as_posix()} does not exist")
        elif not r.is_break:
            findings.append(f"week {r.week}: has no lecture, is not an MCQ and is not the reading week")
        if r.lab and not (LABS / r.lab / "README.md").is_file():
            findings.append(f"week {r.week}: labs/{r.lab}/README.md does not exist")

    for d in sorted(p.name for p in LECTURES.iterdir() if p.is_dir()):
        if d not in claimed_decks:
            findings.append(f"lectures/{d}/ is not in module/schedule.json, so it would not be on the site")
        if re.search(r"week-?\d", d):
            findings.append(f"lectures/{d}/: folder names carry no week number; the schedule does")
    if MCQ.is_dir():
        for d in sorted(p.name for p in MCQ.iterdir() if p.is_dir()):
            if d not in claimed_pages:
                findings.append(f"mcq/{d}/ is not in module/schedule.json")

    for deck in sorted(LECTURES.glob("*/slides.md")):
        text = deck.read_text(encoding="utf-8")
        if re.search(r"(?m)^week:", text):
            findings.append(f"{deck.as_posix()}: frontmatter must not declare week: (the schedule does)")
        if re.search(r'class="kicker">// week \d', text):
            findings.append(f"{deck.as_posix()}: the title kicker must not state a week number")
    for r in sched.rows:
        if r.page and r.page.is_file():
            first = r.page.read_text(encoding="utf-8").splitlines()[0]
            if re.search(r"[Ww]eek \d", first):
                findings.append(f"{r.page.as_posix()}: the title must not state a week number")

    readme = README.read_text(encoding="utf-8")
    m = TABLE_RE.search(readme)
    if not m:
        findings.append("README.md: schedule-table markers are missing")
    else:
        committed = re.sub(r"\*\*➡️ (.*?)\*\*", r"\1", m.group(1)).strip()
        if committed != update_current_week.render_table(sched, None).strip():
            findings.append("README.md: the schedule table is stale; run scripts/update_current_week.py")

    topics = [r.topic for r in sched.rows if r.deck]
    cells = []
    for line in OVERVIEW.read_text(encoding="utf-8").splitlines():
        m2 = re.match(r"^\|\s*([^|]+?)\s*\|", line)
        if m2 and m2.group(1) not in ("Topic", "---"):
            cells.append(re.sub(r"&amp;", "&", m2.group(1)).strip("* "))
    last = -1
    for t in topics:
        idx = next((i for i, c in enumerate(cells) if c == t), None)
        if idx is None:
            findings.append(f"{OVERVIEW.as_posix()}: no row for '{t}' in the topic table")
        elif idx < last:
            findings.append(f"{OVERVIEW.as_posix()}: '{t}' is out of schedule order")
        else:
            last = idx

    labs_readme = Path("labs/README.md").read_text(encoding="utf-8")
    scheduled = [r.lab for r in sched.rows if r.lab]
    listed = re.findall(r"(?m)^\| \[([a-z0-9-]+)\]\(\1/\) \|", labs_readme)
    if listed != scheduled:
        findings.append(f"labs/README.md: the labs table must list the scheduled labs in "
                        f"schedule order; expected {scheduled}, found {listed}")

    if findings:
        print("\n".join("check_schedule: " + f for f in findings))
        sys.exit(1)
    how = "derived from the October bank holiday" if sched.derived else "from startDate"
    print(f"check_schedule: {len(sched.rows)} rows; week 1 begins {sched.start} ({how}); every view agrees")


if __name__ == "__main__":
    main()
