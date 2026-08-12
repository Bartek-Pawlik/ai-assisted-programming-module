"""A small summarising feature — the non-deterministic half of this lab.

Section 4 asks you to test this. You cannot do it the way you test
`hello_app`, because the same input does not produce the same output.

Runs offline by default so nobody needs a key or a budget. The stand-in
model below is deliberately non-deterministic in the same way a real one
is: it picks among several acceptable phrasings. Everything you learn
about testing it transfers directly to a real model, because the problem
is the variability, not the provider.

    python summarise.py samples/article_1.txt
"""
import random
import re
import sys
from pathlib import Path

# TODO (DIY 6): this is the prompt you will try to improve. Change it,
# re-run the whole eval set, and find out whether you actually helped.
PROMPT = "Summarise the article in one sentence."

TEMPLATES = [
    "{subject} {verb} {figure}{tail}.",
    "{figure}: {subject} {verb}{tail}.",
    "The main point is that {subject} {verb} {figure}{tail}.",
]
VERBS = ["rose", "grew", "increased by", "was up"]
TAILS = ["", " on renewals", " year on year", " across all regions"]


def _key_figure(text: str) -> str:
    """The first percentage or number in the text, if there is one."""
    m = re.search(r"\b\d+(?:\.\d+)?%|\b\d[\d,]*\b", text)
    return m.group(0) if m else ""


def _subject(text: str) -> str:
    first = next((ln for ln in text.splitlines() if ln.strip()), "")
    return first.split(" ")[0].strip(".,") or "It"


def summarise(text: str) -> str:
    """Return a one-sentence summary.

    Non-deterministic ON PURPOSE. Two calls with the same input can return
    different wording, both correct. That is the property section 4 is
    about, and it is why an equality assertion is the wrong tool.
    """
    template = random.choice(TEMPLATES)
    return template.format(
        subject=_subject(text),
        verb=random.choice(VERBS),
        figure=_key_figure(text),
        tail=random.choice(TAILS),
    ).replace("  ", " ")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python summarise.py <file>")
        return 2
    print(summarise(Path(sys.argv[1]).read_text(encoding="utf-8")))
    return 0


if __name__ == "__main__":
    sys.exit(main())
