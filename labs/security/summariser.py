"""A document summariser with a prompt-injection hole. DIY 5.

This stands in for the AI feature in your own project: it takes text a
user supplied and puts it in front of a model. Any text a user supplies
can contain instructions.

Run it on a clean document and it behaves. Run it on the poisoned one and
watch what the document tells it to do:

    python summariser.py documents/clean.txt
    python summariser.py documents/poisoned.txt

Your job in DIY 5 is to change SYSTEM_PROMPT and build_messages() so the
document is treated as data and not as orders -- then to try to defeat
your own fix.

No API key is needed. `--offline` (the default when no key is set) uses a
deliberately naive stand-in model so the injection is visible without
anyone paying for tokens.
"""
import os
import sys

# TODO (DIY 5, step 4): this instruction is too weak. It says what to do
# but never says that the document is untrusted, never marks where the
# document starts and ends, and never tells the model what to do when the
# document tries to give it orders.
SYSTEM_PROMPT = "Summarise the document the user gives you in one sentence."


def build_messages(document: str) -> list[dict]:
    """Assemble what gets sent to the model.

    Note what is wrong here: the document is concatenated straight into
    the user turn, so from the model's side there is nothing separating
    'the thing to summarise' from 'an instruction to follow'. Everything
    arrives as one undifferentiated stream of text.
    """
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": document},
    ]


def naive_model(messages: list[dict]) -> str:
    """A stand-in that mimics an instruction-following model.

    Real models are far better than this, and still fall for well-built
    injections. This one is exaggerated on purpose so the failure is
    unmistakable without needing a key: it scans the text for anything
    that looks like an instruction and obeys the last one it finds.
    """
    document = messages[-1]["content"]
    lowered = document.lower()
    for marker in ("ignore all previous instructions",
                   "ignore your previous instructions",
                   "disregard the above"):
        if marker in lowered:
            after = document[lowered.index(marker) + len(marker):].strip()
            return f"[model obeyed the document] {after.splitlines()[0][:120]}"
    first = next((ln for ln in document.splitlines() if ln.strip()), "")
    return f"[summary] {first[:120]}"


def summarise(document: str) -> str:
    if os.environ.get("OPENAI_API_KEY"):
        # Left for you if you want to try it against a real model. The
        # injection behaves the same way; it is just less obvious.
        print("(a real key is set, but this lab runs offline by design)",
              file=sys.stderr)
    return naive_model(build_messages(document))


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python summariser.py <document>")
        return 2
    document = open(sys.argv[1], encoding="utf-8").read()
    print(summarise(document))
    return 0


if __name__ == "__main__":
    sys.exit(main())
