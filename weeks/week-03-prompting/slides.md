---
title: Prompting and Context Engineering
week: 3
topic: prompting
type: lecture
source: authored
marp: true
theme: aiap
paginate: true
transition: fade
---

<!-- Speaker notes: ~0:01. Title while they settle.

Two halves, and the join is the point of the hour: prompting (how you ask)
was the whole skill in 2023; context engineering (what the model can see)
is the larger half now. Do not treat the second as an advanced extra —
it is where most real failures live. -->

<!-- _class: lead -->

<span class="kicker">// how you ask, and what it can see</span>

# Prompting and Context Engineering

---

<!-- Speaker notes: ~0:02. The hook. Put both up, take a vote, do NOT
reveal yet.

Nearly everyone votes B, and they are right — but for the wrong reason.
They will say "because it's more detailed". The actual reason is that B
makes a DECISION the model would otherwise have to guess. That distinction
is the hour's first idea and it is revealed two slides on. -->

## Two prompts, same task

<p class="prompt bad">write a function to parse a date string</p>

<p class="prompt good">Write a Python function parse_date(s: str) -> date.
Accept "2026-08-12" and "12/08/2026" (day first). Raise ValueError on
anything else. No external libraries.</p>

* Which gets the better answer — and **why**?

---

<!-- Speaker notes: ~0:04. The idea. Say it once, plainly, then move.

The misconception to kill immediately: students think a good prompt is a
LONG prompt, and start padding. Length is not the variable. Decisions
made, and information supplied, are the variables. -->

## The one idea

<div class="callout">

A prompt is not a request. It is a **specification**. Everything you leave
unspecified, the model decides for you — silently, and from whatever was
most common in its training data.

</div>

* "Better prompt" does not mean "longer prompt"

---

<!-- Speaker notes: ~0:05. Agenda. Reference slide, brisk. Flag the second
half explicitly — it is the part that is new this year. -->

## This hour

- What a prompt actually is, mechanically
- SPEC: a recipe you can apply every time
- Constraints and non-goals
- Persona, chain-of-thought, few-shot
- **Context engineering** — the half that is not about wording
- Where prompting cannot help you

---

<!-- Speaker notes: ~0:07. Tokens. Keep this SHORT and make it earn its
place — this is not a machine-learning lecture. They need tokens only so
that context windows and cost make sense.

Useful live demo if the clock allows: a tokeniser playground, paste in a
variable name in camelCase and watch it shatter into four tokens. -->

## Tokens: the unit it actually reads

* A token is a chunk of text — a word, part of a word, or punctuation

- `"Programming"` → `Pro` + `gram` + `ming`
- Everything is priced, limited, and remembered **in tokens**

<div class="callout">

Rough rule: **one token ≈ ¾ of a word** in English. Code is denser —
identifiers and punctuation fragment heavily.

</div>

---

<!-- Speaker notes: ~0:09. Context window. THIS is the slide that makes
context engineering make sense later, so spend the time.

The framing that sticks: short-term memory with a hard edge. Everything
inside can influence the answer; everything outside may as well not exist.
There is no partial credit for "I told you earlier" if earlier fell out. -->

## The context window

<div class="stack">
  <div class="layer top"><span>System instruction + your prompt</span><span class="rank">in</span></div>
  <div class="layer"><span>Files, errors, docs you pasted</span><span class="rank">in</span></div>
  <div class="layer"><span>The conversation so far</span><span class="rank">in</span></div>
  <div class="layer untrusted"><span>Everything else you know and it does not</span><span class="rank">invisible</span></div>
</div>

* It is short-term memory with a **hard edge**

* Inside, it can influence the answer. Outside, it does not exist

---

<!-- Speaker notes: ~0:12. SPEC. The recipe, and the thing they will
actually use every day. Four letters, one slide.

Say that any framework works and the discipline matters more than the
acronym — but pick one and stay with it, because switching frameworks is a
way of avoiding the work. -->

## SPEC — a recipe for every prompt

| | | Example |
|---|---|---|
| **S** | Specific goal | "Parse a date string into a `date`" |
| **P** | Programming language / file | "Python 3.12, in `utils/dates.py`" |
| **E** | Example, input → output | `"2026-08-12"` → `date(2026, 8, 12)` |
| **C** | Constraints | "No external libraries. Raise on bad input" |

<span class="kicker">// other frameworks exist; the discipline matters more than the acronym</span>

---

<!-- Speaker notes: ~0:15. Back to the opening pair, now analysable.
Walk B through SPEC letter by letter and let them see all four present.

Then the payoff line: the difference is not detail, it is DECISIONS. Day
first or month first? That is a product decision, and the vague prompt
hands it to a text predictor. -->

## The opening pair, decoded

<p class="prompt good">Write a Python function parse_date(s: str) -> date.
Accept "2026-08-12" and "12/08/2026" (day first). Raise ValueError on
anything else. No external libraries.</p>

- **S** parse a date · **P** Python, typed signature
- **E** two formats shown · **C** raises, no dependencies

<div class="callout">

`12/08/2026` — is that August or December? The vague prompt hands that
decision to a text predictor. **That** is the difference, not the length.

</div>

---

<!-- Speaker notes: ~0:18. Constraints and non-goals. Non-goals are the
under-used half and the one that saves them most pain.

The misconception: students think an assistant that adds extra things is
being helpful, so they tolerate it. In a review, unrequested changes are
where real defects hide — they are the changes nobody was looking at. -->

## Constraints and non-goals

**Constraints** — the boundaries the answer must respect:

- `Python 3.12` · `no new dependencies` · `under 200ms` · `no eval()`

**Non-goals** — what it must *not* touch:

- ❌ no database schema changes
- ❌ no error handling yet
- ❌ do not reformat the rest of the file

<div class="callout">

Assistants **over-deliver**. Unrequested changes are where defects hide,
because they are the changes nobody was reviewing.

</div>

---

<!-- Speaker notes: ~0:21. PREDICT beat 1. Show the code, ask what the
assistant does with this prompt. Vote before revealing.

The wrong answer to expect is "it just fixes the bug". Students assume a
narrow ask produces a narrow change. In practice, given a whole file and a
vague instruction, assistants commonly reformat, rename, add type hints
and add try/except — and the one-line fix is buried in a 40-line diff
nobody reads carefully. That is the argument for non-goals, made by
experience rather than assertion. -->

## Predict: what comes back?

<p class="prompt bad">here's my file, fix the bug in calculate_total</p>

* Just the fixed function
* The fixed function, plus type hints it added
* The whole file, reformatted, with error handling added
* All of the above, in one 40-line diff

---

<!-- Speaker notes: ~0:24. The reveal — usually the last option. Then the
fix, which is one sentence of non-goal.

Land the review point: a 3-line diff gets read. A 40-line diff gets
skimmed. The size of your diff determines whether review actually
happened. -->

## Usually the biggest one

* Ask narrowly, and say what **not** to touch

<p class="prompt good">Fix only the off-by-one in calculate_total.
Change nothing else — no formatting, no type hints, no error handling.
Show me a diff, not the file.</p>

<div class="callout">

A 3-line diff gets **read**. A 40-line diff gets **skimmed**. You choose
which one you are reviewing when you write the prompt.

</div>

---

<!-- Speaker notes: ~0:27. The three advanced techniques, one slide each
would be too slow — keep them together and let the lab drill them.

Say what each is FOR, because students collect techniques without knowing
when to reach for them. Persona = shifts attention. CoT = multi-step
correctness. Few-shot = exact output format. -->

## Three techniques worth knowing

| Technique | What it does | Reach for it when |
|---|---|---|
| **Persona** | Shifts what it pays attention to | You want a specific lens — security, performance |
| **Chain-of-thought** | Asks for the steps, not just the answer | Correctness depends on intermediate results |
| **Few-shot** | Shows examples instead of describing | Output **format** must be exact |

<span class="kicker">// collect techniques, but know which problem each one solves</span>

---

<!-- Speaker notes: ~0:30. The turn. Everything so far has been about
WORDING. This is where the hour pivots, and it is the newest material.

Set it up with the honest history: models got much better at inferring
intent from sloppy requests, so the marginal value of rewording fell. What
they still cannot do is invent information they were never given. -->

## The turn: it is not mostly about wording

* Models got **much better** at inferring intent from a sloppy request

* So the value of polishing wording fell

<div class="callout">

What they still cannot do is **invent information they were never given.**

</div>

- The bottleneck moved from *how you ask* to *what it can see*

---

<!-- Speaker notes: ~0:33. The definition, and the comparison table that
makes it concrete. This is the slide to photograph.

Emphasise the last row — prompt engineering optimises a human talking to a
model; context engineering optimises an agent working with one. As agents
do more, the second matters more. -->

## Context engineering

| | Prompt engineering | Context engineering |
|---|---|---|
| Question | How do I phrase this? | What does it need to see? |
| You tune | Wording, structure, examples | Files, schemas, errors, prior code |
| Fails when | The request is ambiguous | It is missing something it cannot guess |
| Optimises | Human → model | Agent → model |

---

<!-- Speaker notes: ~0:35. PREDICT beat 2 — the diagnostic, and the most
practically useful thirty seconds of the hour.

The wrong answer to expect is "reword it again" — it is what everyone
does, and it is why people spend twenty minutes going nowhere. Consistent
failure across rewordings is EVIDENCE: the problem is missing information,
not phrasing. No amount of rewording adds information. -->

## Predict: you reworded it three times and it is still wrong

What does that tell you?

* The model is not good enough — try a bigger one
* Keep rewording, you will find the magic phrasing
* **It is missing something it cannot guess**
* Raise the temperature for more variety

---

<!-- Speaker notes: ~0:38. The answer and the rule. This is the sentence
to leave on the board.

Then the counter-intuitive half: MORE context is not better. A huge
irrelevant paste makes answers worse — attention gets diluted, and models
attend less reliably to the middle of very long inputs. Context
engineering is as much about exclusion as inclusion. -->

## Ask the diagnostic question

<div class="callout">

*Is this wrong because I **asked** badly, or because it does not **know**
something?*

</div>

* Wording problem → rewrite the prompt

* Knowledge problem → paste the schema, the error, the failing test

- And **more is not better**: a huge irrelevant paste dilutes the relevant
  part and makes answers worse

---

<!-- Speaker notes: ~0:41. Professional practice. These four are what
separates someone using an assistant well from someone typing at it.

Tests-first is the one worth dwelling on: it converts "looks right" into
"passes", which is the same move that lets anyone stop reading generated
code line by line. If the room has met that argument already, call back to
it here. -->

## Four habits worth building

- **Ask for clarifying questions first** — surfaces the assumptions it
  would otherwise make silently
- **Tests first** — specify behaviour as tests, then ask for code that
  passes them
- **Diffs, not files** — you review a change, not a rewrite
- **Give it the real context** — the file, the error, the schema, not your
  summary of them

---

<!-- Speaker notes: ~0:43. Limits. Be blunt: no amount of prompting fixes
these, and pretending otherwise wastes their time.

The last bullet is the honest one — a well-prompted answer to the wrong
question is still wrong, and the assistant will never tell you that you
asked the wrong question. -->

## What prompting cannot fix

- It has **no access** to anything you did not give it
- It has a **training cutoff** — recent library changes are invisible
- It cannot count reliably, and it cannot do arithmetic reliably
- It will confidently answer a question you **should not have asked**

<span class="kicker">// prompting is a steering wheel, not an engine</span>

---

<!-- Speaker notes: ~0:45. Common mistakes. Five behaviours, in the order
they will hit them.

The first one is the commonest and the easiest to fix: padding a prompt
with adjectives instead of decisions. "Write a really good, robust,
professional function" specifies nothing. -->

## Common mistakes

* Padding with adjectives instead of **decisions** — "robust",
  "professional" and "clean" specify nothing

* Rewording when the real problem is missing information

- Pasting far more context than the question needs
- Accepting a large diff because the change you asked for is somewhere in it
- Collecting frameworks instead of picking one and using it

---

<!-- Speaker notes: ~0:47. Summary and close. Return to the opening pair
and ask the room to explain the difference now — they should say
"decisions", not "detail".

Leave the callout up through questions. -->

## Summary

- A prompt is a **specification**. What you leave out, it decides for you
- **SPEC** — specific goal, language, example, constraints — every time
- **Non-goals** keep the diff small enough to actually review
- Persona shifts attention, chain-of-thought helps multi-step, few-shot
  fixes format
- **Context engineering** is the larger half now: not how you ask, but
  what it can see — and more is not better

<div class="callout">

*Is it wrong because I asked badly, or because it doesn't know something?*
No amount of rewording adds information.

</div>
