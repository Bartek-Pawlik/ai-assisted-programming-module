---
title: Coding Agents
week: 6
topic: agents
type: lecture
source: authored
marp: true
theme: aiap
paginate: true
transition: fade
---

<!-- Speaker notes: ~0:01. Title while they settle.

The spine of this hour is a LADDER, and the skill being taught is picking
a rung deliberately. Students arrive with one of two defaults — always the
most autonomous, or never — and both are unexamined. -->

<!-- _class: lead -->

<span class="kicker">// from answering to acting</span>

# Coding Agents

---

<!-- Speaker notes: ~0:02. The hook. Read all three out and ask what
changed between them. Take answers.

The answer people give is "it got smarter". The answer that matters is
"it got PERMISSION". Same model in all three cases. Do not reveal yet. -->

## Three requests

<p class="prompt">What does this function do?</p>

<p class="prompt">Rewrite this function to handle empty input.</p>

<p class="prompt">Make the test suite pass.</p>

* Same model, same day. What changed?

---

<!-- Speaker notes: ~0:04. The idea, and the reframe the hour turns on.

The misconception to kill: students believe agent mode is a smarter model.
It is not — it is the same model with permission to act and to loop. That
distinction matters because it tells you where to look when it goes wrong:
not "the model was dumb" but "I gave it the wrong amount of rope". -->

## The one idea

<div class="callout">

It is not a smarter model. It is the **same model with permission to act**
— and to keep going until it decides it is done.

</div>

* What changes across the ladder is **authority**, not intelligence

* So the question is never "can it?" — it is "how much rope?"

---

<!-- Speaker notes: ~0:05. Agenda. Brisk. -->

## This hour

- The ladder: answer → edit → act
- What review means at each rung
- Terminal agents: more reach, more risk
- When more autonomy is the wrong choice
- Reviewing work you did not watch

---

<!-- Speaker notes: ~0:07. The ladder itself. THE slide of the hour — put
it up and leave it up while you walk each rung.

The right-hand column is the payload: what you are actually reviewing
changes at every rung, and most people never notice it changed. -->

## The ladder

| Rung | It may | You review |
|---|---|---|
| **Ask** | Answer only. Touch nothing | A suggestion |
| **Edit** | Change a selection you chose | A diff |
| **Agent** | Choose files, make changes, run things | A result |
| **Terminal agent** | All of that, across a whole repo | A result, and a trail |

<span class="kicker">// the unit of review changes at every rung</span>

---

<!-- Speaker notes: ~0:10. Ask mode, and a defence of it — students skip
it because it feels slow.

The argument: it is the only rung where the output lands in your HEAD
rather than in your files. Everything above it assumes you already
understand the code well enough to judge a change. Understanding is the
step that gets skipped, and it is the one that does not survive skipping. -->

## Ask: the rung people skip

* It answers. It cannot touch a single file

* Every change is still one **you** make

<div class="callout">

The only rung where the output lands in your **head** rather than in your
files. Every rung above assumes you already understand the code.

</div>

- Best tool in the room for code you did not write

---

<!-- Speaker notes: ~0:12. Edit mode and the diff. Short section — the
important content is the next slide's predict beat. -->

## Edit: the diff is the safety mechanism

* You select, you describe the change, it rewrites in place

* You accept or reject a **diff**

- The diff is not a formality. It is the entire safety mechanism at this
  rung

---

<!-- Speaker notes: ~0:14. PREDICT beat 1. Vote before revealing.

The wrong answer to expect is "just the rename". Students assume a narrow
instruction produces a narrow change. In practice assistants tidy while
they are in there: imports reordered, type hints added, a docstring
rewritten, a stray reformat. None of that was asked for, and all of it is
inside the diff you are about to approve. -->

## Predict: you ask for one rename

<p class="prompt bad">rename calculate to compute_total in this file</p>

What comes back?

* Exactly that rename, nothing else
* The rename, plus reordered imports and a few added type hints
* A full rewrite of the file
* It asks a clarifying question first

---

<!-- Speaker notes: ~0:17. The reveal — usually the tidying. Then the
rule, which is the practical takeaway of the whole edit section.

Say the sentence about diff size out loud; it is the one people repeat
back. -->

## It tidies while it is in there

* Say what must **not** change, not just what must

<p class="prompt good">Rename calculate to compute_total in this file.
Change nothing else: no import reordering, no type hints, no reformatting.</p>

<div class="callout">

A 3-line diff gets **read**. A 40-line diff gets **skimmed**. You choose
which you are reviewing when you write the prompt.

</div>

---

<!-- Speaker notes: ~0:19. Agent mode. The genuine step change, and the
thing to be clear about: you stop reviewing a change and start reviewing
a RESULT.

The practical consequence is the second bullet — you must be able to say
what "done" means BEFORE you start, or you cannot tell whether it got
there and you will accept whatever looks finished. -->

## Agent: describing outcomes, not steps

* You give a **goal**. It works out the files, the changes, the commands

* You review a **result**, not a change

<div class="callout">

If you cannot say what "done" means **before** it starts, you cannot tell
whether it got there — and you will accept whatever looks finished.

</div>

---

<!-- Speaker notes: ~0:22. PREDICT beat 2, and the most useful thirty
seconds of the hour for their own agent work.

The wrong answer to expect is "the detailed one, obviously" — students
transfer the SPEC lesson wholesale and assume more specification is always
better. At this rung it inverts: prescribing steps wastes exactly what
agent mode is for, and worse, it will follow your bad plan faithfully.
Specify the OUTCOME and the constraints precisely; leave the route open. -->

## Predict: which works better in agent mode?

<p class="prompt bad">Open utils.py, find the parse function, add a try/except
around line 40, then open test_utils.py and add a test, then run pytest.</p>

<p class="prompt good">Make parse() handle malformed input without crashing.
Add a test covering it. All existing tests must still pass.</p>

---

<!-- Speaker notes: ~0:24. The reveal and the distinction — this is
subtle and worth the time.

Precision moves from the ROUTE to the DESTINATION. Be vague about how, be
ruthless about what done means. Students find this counter-intuitive after
a whole lecture on specific prompts, so name the tension explicitly. -->

## The second — and this inverts the usual rule

* Prescribing steps wastes what the rung is **for**

* And it will follow your bad plan faithfully

<div class="callout">

Precision moves from the **route** to the **destination**. Vague about
*how*; ruthless about what *done* means.

</div>

---

<!-- Speaker notes: ~0:27. Terminal agents. The distinction that matters
is scope, not capability.

An editor agent works in the file you have open. A terminal agent has your
shell and your whole repository. Same instruction, very different blast
radius. -->

## Terminal agents

| | Editor agent | Terminal agent |
|---|---|---|
| Sees | The files you opened | The whole repository |
| Can run | Limited, sandboxed | Your shell |
| Good for | A change you can picture | A change spread across many files |
| Blast radius | The file | Everything |

* Same instruction. Very different consequences

---

<!-- Speaker notes: ~0:29. The discipline. Short and practical — these
are the four habits that make higher rungs survivable.

Commit first is the one to insist on. Without a clean starting point,
`git diff` is not a review tool and `git checkout` is not an undo, and
they have neither. -->

## The discipline for higher rungs

<div class="flow">
  <div class="step"><span class="n">01</span>Commit first — clean starting point</div>
  <div class="step"><span class="n">02</span>Say what done means</div>
  <div class="step"><span class="n">03</span>Let it work, uninterrupted</div>
  <div class="step"><span class="n">04</span>Review the diff, not the story</div>
</div>

<div class="callout">

Without a commit, `git diff` is not a review tool and `git checkout` is
not an undo. You have neither.

</div>

---

<!-- Speaker notes: ~0:32. Review the diff, not the story. This deserves
its own beat because it is the subtlest failure at high autonomy.

An agent reports what it INTENDED. The summary is fluent, confident and
generated from the same process that produced the code. It is not
evidence. The diff is evidence. -->

## The agent's summary is not evidence

* It reports what it **intended** to do

* Fluent, confident, and produced by the same process that wrote the code

<div class="callout">

Read the **diff**, not the summary. And check the files it touched that
you were not expecting — that list is where the surprises live.

</div>

---

<!-- Speaker notes: ~0:34. PREDICT beat 3. The honest one about where
autonomy costs you.

The wrong answer to expect is "the big refactor" — it sounds hardest. In
practice agents do sweeping mechanical changes well. Where they burn time
is the subtle bug with an unclear cause: the agent tries something, it
does not work, it tries something else, and twenty minutes later you have
a pile of speculative changes and no diagnosis. Debugging wants ask mode. -->

## Predict: where does autonomy cost you most?

* A large mechanical refactor across 30 files
* A subtle bug whose cause you do not understand yet
* Writing tests for existing code
* Generating boilerplate

---

<!-- Speaker notes: ~0:37. The reveal. Unknown-cause debugging is the
trap, and the reason is worth stating: an agent optimises for making the
symptom go away, and you wanted a diagnosis.

This is the strongest practical argument in the hour for choosing a LOWER
rung deliberately. -->

## The bug you do not understand yet

* An agent will try things until the symptom disappears

* You wanted a **diagnosis**. It optimises for a green test

<div class="callout">

Twenty minutes later: a pile of speculative changes, a passing test, and
nobody knows what was wrong. Debugging an unknown cause wants **ask**
mode.

</div>

---

<!-- Speaker notes: ~0:39. Common mistakes. Five, ordered by how often
they will hit them.

The last one connects to the whole hour: reaching for the top rung by
default is the same unexamined choice as never leaving the bottom one. -->

## Common mistakes

* Reviewing the **summary** instead of the diff

* Prescribing steps in agent mode, then blaming it for following them

- Not committing first, so there is no undo and no review surface
- Using an agent to debug something nobody has diagnosed
- Defaulting to the top rung — as unexamined as never leaving the bottom

---

<!-- Speaker notes: ~0:42. Summary and close. Return to the three
requests from the start and ask the room what changed — they should say
"permission", not "intelligence".

Leave the callout up for questions. -->

## Summary

- The ladder is **answer → edit → act**, and what changes is **authority**
- What you review changes at every rung: suggestion, diff, result
- Say what must **not** change, so the diff stays small enough to read
- In agent mode, precision moves from the **route** to the **destination**
- Terminal agents have a bigger blast radius for the same instruction
- The summary is not evidence. The diff is

<div class="callout">

Pick the rung deliberately: how reversible is it, how well can you test
it, and what does being wrong cost?

</div>
