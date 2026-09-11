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

The module introduction is a partial exception, not an exemption. It may
talk about its own schedule ("week 7", "the module") and link to its own
site and repository -- that is what an introduction is for -- but it must
not name an institution, a lecturer, a VLE or a course code any more than
the other decks: a lecturer at another college should be able to present
it after swapping two links. So it is checked for IDENTITY only, with URLs
blanked out first.

Run from the repo root:  python scripts/check_deck_portability.py
"""
import re
import sys
from pathlib import Path

WEEKS = Path("weeks")

# The introduction: identity rules apply, schedule rules do not.
INTRO = "week-01-introduction"
URL_RE = re.compile(r"https?://\S+")

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


def check(deck: Path, identity_only: bool = False) -> list[str]:
    text = deck.read_text(encoding="utf-8")
    text = FRONTMATTER_WEEK.sub("", text, count=1)
    patterns = IDENTITY if identity_only else {**IDENTITY, **SCHEDULE}

    findings = []
    for lineno, line in enumerate(text.split("\n"), start=1):
        # The introduction may link to its own site and repo; the link is
        # the thing another lecturer swaps, so it is not a portability fault.
        scan = URL_RE.sub("", line) if identity_only else line
        for label, pattern in patterns.items():
            m = pattern.search(scan)
            if m:
                findings.append(
                    f"{deck.as_posix()}:{lineno}: {label} -> {m.group(0)!r}")
    return findings


def main() -> int:
    if not WEEKS.is_dir():
        return 0
    decks = sorted(WEEKS.glob("week-*/slides.md"))
    findings = []
    for deck in decks:
        findings.extend(check(deck, identity_only=(deck.parent.name == INTRO)))

    for line in findings:
        print(line)
    if findings:
        print(f"\n{len(findings)} portability problem(s). Every deck must be "
              f"teachable by another lecturer in another college, unchanged; "
              f"the introduction may state its own schedule and links but "
              f"not its institution.", file=sys.stderr)
        return 1

    print(f"check_deck_portability: {len(decks)} deck(s) are self-contained "
          f"(the introduction checked for identity only)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
