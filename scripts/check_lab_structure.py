#!/usr/bin/env python3
"""Enforce the lab README formula (see CLAUDE.md, "Lab formula").

These labs arrived by migration from nine separate GitHub Classroom repos
written by different hands at different times, so they disagreed about
almost everything: Task vs Part vs Exercise, whether hints existed, whether
a student could self-check at all. A student meeting a new lab each week
should not have to relearn where things are.

The required shape:

    # <title>
    ## What you'll learn
    ## Table of Contents
    ## Getting started
    ... numbered sections, each with `### DIY k: <name>` exercises ...
    ## Summary                                    <- LAST heading

and every `### DIY k` must carry all three of:

    1. numbered steps
    2. `**What you should have**` or `**Expected output**`
    3. a hint in <details><summary>Hint</summary>

CONFORMING is the exemption list, inverted on purpose. A lab is checked
only once it appears there, so the gate can land green today and each lab
gets held to the formula the moment it is rewritten. The list must GROW to
cover every lab; a lab that regresses out of conformance fails the build.

Run from the repo root:  python scripts/check_lab_structure.py
"""
import re
import sys
from pathlib import Path

LABS = Path("labs")

# Labs rewritten to the formula and now enforced. ADD TO THIS as each lab is
# reworked -- never remove an entry to make a failure go away.
CONFORMING = {
    "security",
    "agents",
}

REQUIRED_SECTIONS = ("What you'll learn", "Table of Contents",
                     "Getting started", "Summary")

H2_RE = re.compile(r"(?m)^##\s+(?:[^\w\s]+\s*)?(.+?)\s*$")
DIY_RE = re.compile(r"(?m)^###\s+DIY\s+(\d+):\s*(.+?)\s*$")
STEP_RE = re.compile(r"(?m)^\s*\d+\.\s+\S")
DELIVERABLE_RE = re.compile(r"\*\*(?:What you should have|Expected output)\*\*")
HINT_RE = re.compile(r"<details>\s*<summary>\s*(?:<[^>]+>\s*)?Hint",
                     re.IGNORECASE)


def section_bodies(text: str) -> list[tuple[str, str]]:
    """(diy_label, body) for each DIY block, body running to the next heading."""
    out = []
    matches = list(DIY_RE.finditer(text))
    for i, m in enumerate(matches):
        start = m.end()
        # A DIY body ends at the next heading of ANY level -- the next DIY,
        # or the section that follows it.
        nxt = re.compile(r"(?m)^#{2,3}\s+").search(text, start)
        end = nxt.start() if nxt else len(text)
        if i + 1 < len(matches):
            end = min(end, matches[i + 1].start())
        out.append((f"DIY {m.group(1)}: {m.group(2)}", text[start:end]))
    return out


def check_lab(lab: Path) -> list[str]:
    readme = lab / "README.md"
    if not readme.is_file():
        return [f"{lab.as_posix()}: no README.md"]

    text = readme.read_text(encoding="utf-8")
    rel = readme.as_posix()
    findings: list[str] = []

    if not re.match(r"^#\s+\S", text):
        findings.append(f"{rel}: must open with a level-1 heading")

    headings = [h.strip() for h in H2_RE.findall(text)]
    for required in REQUIRED_SECTIONS:
        if not any(h.lower().startswith(required.lower()) for h in headings):
            findings.append(f"{rel}: missing `## {required}` section")

    if headings and not headings[-1].lower().startswith("summary"):
        findings.append(
            f"{rel}: `## Summary` must be the LAST section (found "
            f"`## {headings[-1]}` after it)")

    diys = section_bodies(text)
    if not diys:
        findings.append(f"{rel}: no `### DIY k: <name>` exercises found")

    numbers = [int(m.group(1)) for m in DIY_RE.finditer(text)]
    if numbers and numbers != list(range(1, len(numbers) + 1)):
        findings.append(
            f"{rel}: DIY numbering must run 1..n with no gaps, got {numbers}")

    for label, body in diys:
        if not STEP_RE.search(body):
            findings.append(f"{rel}: {label} has no numbered steps")
        if not DELIVERABLE_RE.search(body):
            findings.append(
                f"{rel}: {label} has no `**What you should have**` or "
                f"`**Expected output**` block — the student cannot self-check")
        if not HINT_RE.search(body):
            findings.append(f"{rel}: {label} has no <details> Hint block")
    return findings


def main() -> int:
    if not LABS.is_dir():
        print("check_lab_structure: no labs/ directory")
        return 0

    all_labs = sorted(p.name for p in LABS.iterdir() if p.is_dir())
    unknown = CONFORMING - set(all_labs)
    if unknown:
        print(f"check_lab_structure: CONFORMING names a lab that does not "
              f"exist: {', '.join(sorted(unknown))}", file=sys.stderr)
        return 1

    findings: list[str] = []
    for name in all_labs:
        if name in CONFORMING:
            findings.extend(check_lab(LABS / name))

    for line in findings:
        print(line)
    if findings:
        return 1

    pending = [n for n in all_labs if n not in CONFORMING]
    print(f"check_lab_structure: {len(CONFORMING)} lab(s) conform")
    if pending:
        print(f"  not yet rewritten to the formula ({len(pending)}): "
              f"{', '.join(pending)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
