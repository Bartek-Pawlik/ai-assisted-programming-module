#!/usr/bin/env python3
"""Every lecture must be liftable into somebody else's course, unchanged.

The requirement: hand any single week's deck to a lecturer at another
institution and they can teach it, in whatever module they like, without
editing anything. That rules out three kinds of coupling:

  1. WHOSE it is    -- a lecturer's name, an institution, a VLE URL
  2. WHERE it sits  -- "last week", "in week 7", "later in this module"
  3. WHAT it needs  -- a link to a sibling week's folder

(1) and (3) are mechanical and this gate checks them. (2) is checked with
a deliberately narrow pattern, because English is full of innocent uses of
"next week" inside an example, and a gate that cries wolf gets switched
off.

The week-01 deck is EXEMPT and always will be: a module introduction is
inherently about a specific module at a specific institution. It is the
one deck nobody can lift, which is exactly why every other deck must be
liftable. Keep the exemption list at one entry.

Run from the repo root:  python scripts/check_deck_portability.py
"""
import re
import sys
from pathlib import Path

WEEKS = Path("weeks")

# The only deck allowed to be institution-specific. Do not add to this.
EXEMPT = {"week-01-introduction"}

# Identity and institution. Extend if the module changes hands -- the
# point is that NO owner's name appears, not that this one's does not.
IDENTITY = {
    "lecturer or author name": re.compile(r"(?i)\b(daniel\s+cregg|cregg)\b"),
    "institution name": re.compile(
        r"(?i)\b(atlantic\s+technolog\w*|\bATU\b|galway[- ]?mayo|GMIT)\b"),
    "institution or VLE domain": re.compile(
        r"(?i)\b[\w.-]*(atu\.ie|vlegalwaymayo|atugalwaymayo)[\w./-]*"),
    "personal site or module URL": re.compile(
        r"(?i)danielcregg\.[\w.]+|is-a\.dev"),
    "VLE course id": re.compile(r"(?i)\bmoodle\b|\bcourse\s+\d{4,}\b"),
}

# Schedule coupling. Narrow on purpose: only forms that name a NUMBERED
# week, or that position this deck relative to another one.
SCHEDULE = {
    "names a numbered week": re.compile(r"(?i)\bweek\s*\d+\b"),
    "positions itself in a schedule": re.compile(
        r"(?i)\b(last|next|previous|earlier|later)\s+(week|lecture)\b"),
    "refers to the module as a container": re.compile(
        r"(?i)\b(this|the)\s+module\b"),
    "links to another week's folder": re.compile(r"\.\./week-\d"),
}

# Frontmatter `week:` is structural metadata the site build reads, not
# prose a reader ever sees, so it is skipped. Speaker notes ARE checked:
# they ship inside the rendered HTML and another lecturer reads them.
FRONTMATTER_WEEK = re.compile(r"(?m)^week:\s*\d+\s*$")


def check(deck: Path) -> list[str]:
    text = deck.read_text(encoding="utf-8")
    text = FRONTMATTER_WEEK.sub("", text, count=1)

    findings = []
    for lineno, line in enumerate(text.split("\n"), start=1):
        for label, pattern in {**IDENTITY, **SCHEDULE}.items():
            m = pattern.search(line)
            if m:
                findings.append(
                    f"{deck.as_posix()}:{lineno}: {label} -> {m.group(0)!r}")
    return findings


def main() -> int:
    if not WEEKS.is_dir():
        return 0
    decks = sorted(WEEKS.glob("week-*/slides.md"))
    findings, checked = [], 0
    for deck in decks:
        if deck.parent.name in EXEMPT:
            continue
        checked += 1
        findings.extend(check(deck))

    for line in findings:
        print(line)
    if findings:
        print(f"\n{len(findings)} portability problem(s). Every deck except "
              f"the module introduction must be teachable by another lecturer "
              f"in another course, unchanged.", file=sys.stderr)
        return 1

    print(f"check_deck_portability: {checked} deck(s) are self-contained "
          f"({len(EXEMPT)} exempt)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
