---
title: Vibe Coding and Spec-Driven Development
week: 11
topic: vibe-coding
type: lecture
source: authored
marp: true
theme: aiap
paginate: true
transition: fade
---

<!-- Speaker notes: ~0:30. Title while they settle.

This hour is an argument with two sides, not a demonstration of a tool.
Resist letting it become a tools tour — the tools will have changed by
next year and the argument will not. -->

<!-- _class: lead -->

<span class="kicker">// two answers to the same question</span>

# Vibe Coding and Spec-Driven Development

---

<!-- Speaker notes: ~1:30. The hook — the original quote, with its date.

Read it out. It is more radical than students expect, and the phrase
"forget that the code even exists" is doing real work. Note the date:
February 2025. Then note what it became. -->

## Where the phrase came from

> "There's a new kind of coding I call **vibe coding**, where you fully
> give in to the vibes, embrace exponentials, and **forget that the code
> even exists**."

<span class="kicker">// Andrej Karpathy, February 2025</span>

* He was describing a mode he was enjoying

* Not proposing a methodology

---

<!-- Speaker notes: ~3:30. The idea of the hour. State the tension
directly rather than picking a side yet.

The misconception to head off early: students expect a lecture telling
them vibe coding is bad. It is not — it is excellent for the thing it is
good at. The skill is knowing which mode a task deserves, and that is a
judgement, not a rule. -->

## The one idea

<div class="callout">

Both modes are correct. For **different tasks**. The skill is telling
which task you are on — before you start, not afterwards.

</div>

* This hour is an argument, not a verdict

---

<!-- Speaker notes: ~5:00. Agenda. Brisk. -->

## This hour

- What vibe coding is genuinely good at
- What happened when the industry adopted it
- Comprehension debt and haunted codebases
- The counter-trend: spec-driven development
- Choosing a mode, deliberately

---

<!-- Speaker notes: ~6:30. The case FOR, made properly. If you skip this
the room stops listening, because they know these tools work.

The unifying property: all four are situations where being wrong is cheap
because you will throw the artefact away. -->

## What it is genuinely good at

- **Prototypes** — the point is to learn something, then delete it
- **Exploring an unfamiliar stack** — you do not know what to specify yet
- **Throwaway tooling** — a script you will run twice
- **Demos** — where "it works on stage" is the entire requirement

<div class="callout">

The pattern: being wrong is **cheap**, because the artefact is disposable.

</div>

---

<!-- Speaker notes: ~9:30. What happened next. The data slide — expect
photographs, pause.

Read the middle two together. The contradiction is the finding: they do
not trust it, and they ship it anyway. -->

## Then the industry adopted it

| | |
|---|---|
| US developers using AI coding tools daily | **92%** |
| …who say they trust the output | **29%** |
| …who always review before committing | **48%** |
| Major issues vs human-written code | **1.7×** |
| Samples with an OWASP Top-10 vulnerability | **~45%** |
| Sprint capacity on AI-traceable bugs by day 90 | **20–30%** |

<span class="kicker">// treat these as direction, not decimal points</span>

---

<!-- Speaker notes: ~12:30. The provenance caveat, said out loud. This is
a small slide that buys a lot of credibility.

These figures come from 2026 industry surveys of varying rigour that cite
each other. The direction is not in dispute; the second decimal place is
meaningless. Modelling that scepticism out loud is part of the job. -->

## A word on those numbers

* Industry surveys, varying rigour, heavily recycled

* The **direction** is not in dispute. The precision is fiction

<div class="callout">

Being able to say "I believe the trend, not the decimal" is itself an
engineering skill.

</div>

---

<!-- Speaker notes: ~15:00. The two terms. Comprehension debt is the one
to dwell on — it is the technical-debt metaphor applied to understanding.

Ask who has inherited a haunted codebase from their own past self. Most
hands go up, AI or no AI. The point is that AI accelerates the process
rather than inventing it. -->

## Two words worth knowing

<div class="stack">
  <div class="layer top"><span><strong>Comprehension debt</strong> — the future cost of understanding code a machine wrote and nobody read</span><span class="rank">borrowed</span></div>
  <div class="layer untrusted"><span><strong>Haunted codebase</strong> — a working system the team no longer understands</span><span class="rank">the bill</span></div>
</div>

* Technical debt, but what you borrowed against is **understanding**

* AI did not invent this. It accelerated it

---

<!-- Speaker notes: ~18:00. PREDICT beat 1. Vote before revealing.

The wrong answer to expect is "at the start" — students imagine AI-built
projects fail immediately in a visible way. They do not: day one is
euphoric, because the demo works. The cost lands around the point where
you must CHANGE something you did not write -- typically well into a
project, by which point the decisions are baked in. -->

## Predict: when does a vibe-coded project hurt?

* Immediately — it does not work
* Day one is fine; the pain starts when you must **change** it
* Only if you picked the wrong tool
* It does not, if the tests pass

---

<!-- Speaker notes: ~20:30. The reveal. Day one is euphoric. That is
precisely what makes it dangerous — the feedback signal arrives long after
the decision.

The 20-30% figure lands here: by day 90 teams report a fifth to a third of
sprint capacity going on bugs traceable to generated code. -->

## Day one is euphoric

* Which is exactly the problem: the **feedback arrives long after the
  decision**

* You cannot feel comprehension debt accruing. You can only feel it
  arriving

<div class="callout">

By **day 90**, teams report 20–30% of sprint capacity going on bugs
traceable to AI-generated code.

</div>

---

<!-- Speaker notes: ~23:00. The counter-trend. Introduce SDD as a response
rather than as a competing fashion.

The core move: the artefact you review changes from the implementation to
the intent. One page of spec is genuinely easier to judge than 800 lines
of generated code. -->

## The counter-trend: spec-driven development

<div class="flow">
  <div class="step"><span class="n">01</span>Write the spec</div>
  <div class="step"><span class="n">02</span>Agent produces a plan</div>
  <div class="step"><span class="n">03</span>You review the plan</div>
  <div class="step"><span class="n">04</span>Then it implements</div>
</div>

* The artefact you review becomes the **intent**, not the implementation

* One page of spec is easier to judge than 800 lines of generated code

---

<!-- Speaker notes: ~25:30. The two shapes side by side. Short slide,
mostly for the contrast.

Say the honest thing about step 3 in the SDD row: reviewing the plan is
the step people skip, and skipping it turns SDD into vibe coding with
extra paperwork. -->

## The two shapes

```text
Vibe coding:   intent -> code -> hope

Spec-driven:   intent -> spec -> plan -> tasks -> code -> check against spec
```

* Skip the plan review and spec-driven becomes vibe coding **with
  paperwork**

---

<!-- Speaker notes: ~28:00. The honest objection, and this slide is why
the hour is an argument rather than a sermon.

Practitioners genuinely complain that SDD produces piles of markdown to
review instead of code to review — ceremony that feels like rigour. That
criticism is fair and should be stated, not strawmanned. -->

## The honest objection

> "I'd rather review code than all these markdown files."

* Ceremony that **feels** like rigour is not rigour

* A spec nobody reads is worse than no spec: it manufactures confidence

<div class="callout">

Spec-driven has a real cost. If the task does not justify it, the cost is
all you get.

</div>

---

<!-- Speaker notes: ~31:00. PREDICT beat 2. Vote before revealing.

The wrong answer to expect is "spec-driven, always — it's the responsible
one". Students who have absorbed the lecture's warnings over-correct. For
a weekend prototype you intend to delete, writing a specification first is
pure waste: you do not yet know what you want, and finding out is the
point of building it. -->

## Predict: a weekend prototype you intend to delete

Which mode?

* Spec-driven — always the responsible choice
* Vibe coding — you do not know what you want yet
* Spec-driven, but a short spec
* Neither; write it by hand

---

<!-- Speaker notes: ~33:00. The reveal, and the reframe: specification
requires knowledge you may not have yet.

You cannot specify what you have not yet understood. Sometimes building
the thing IS the requirements-gathering. That is a legitimate engineering
position, not laziness. -->

## Vibe coding — and this is not the lazy answer

* You cannot specify what you have not yet understood

* Sometimes building the thing **is** the requirements gathering

<div class="callout">

The failure is not vibe coding. The failure is vibe coding something you
then **keep**.

</div>

---

<!-- Speaker notes: ~35:30. The decision table. THE slide of the hour —
put it up and leave it while you talk.

The bottom row is the sharpest: who maintains this? If the answer is
"somebody, for years", the spec is cheap by comparison. -->

## Choosing, deliberately

| | Vibe coding | Spec-driven |
|---|---|---|
| Stakes | Prototype, demo, throwaway | Production, shared, long-lived |
| Requirements | Discovering them | Known well enough to write |
| Being wrong costs | Delete and retry | Somebody maintains it for years |
| You review | The running app | The spec, then the tests |

---

<!-- Speaker notes: ~38:00. PREDICT beat 3, and the one that lands closest
to home — their own 60% project.

The wrong answer to expect is a single mode for the whole project. The
useful answer is BOTH, at different stages: explore by vibe coding to find
out what you are building, then specify the parts you are keeping. Mode is
per-task, not per-project. -->

## Predict: a large assessed project, built over ten weeks

* Vibe coding — speed matters, deadlines are real
* Spec-driven throughout — the stakes are high
* Vibe the exploration, specify what you keep
* It does not matter as long as it works

---

<!-- Speaker notes: ~40:30. The reveal. Mode is chosen per task, not per
project, and switching deliberately is the mark of someone who understands
both.

Practical instruction for their project: prototype freely, then before you
commit to an architecture, write the page. -->

## Both — and switching on purpose

* Explore by building. Then **write the page** before you commit to it

* Mode is chosen **per task**, not per project

<div class="callout">

If you have to defend it in person, anything you cannot explain is
something you should have specified.

</div>

---

<!-- Speaker notes: ~43:00. Common mistakes. Both directions — over-
correction is as real as under-correction, and the room contains both. -->

## Common mistakes

* Vibe coding something you then **keep**

* Writing a specification for a prototype you will delete on Sunday

- Producing a spec nobody reads, and calling that rigour
- Judging a generated app by whether it runs
- Choosing a mode by habit rather than by task

---

<!-- Speaker notes: ~45:00. Summary and close. Return to Karpathy's quote:
he said "forget that the code even exists", and the hour's answer is that
this is fine right up until you have to change it.

Leave the callout up for questions. -->

## Summary

- Vibe coding is **excellent** where being wrong is cheap and the artefact
  is disposable
- Adoption outran governance: **1.7×** the major issues, **~45%** carrying
  an OWASP Top-10 issue
- **Comprehension debt** is borrowed understanding; the bill arrives when
  you must change something
- **Spec-driven** moves review from implementation to intent — and has a
  real cost of its own
- Choose **per task**: stakes, reversibility, and who maintains it

<div class="callout">

"Forget that the code even exists" is fine — right up to the moment you
have to change it.

</div>
