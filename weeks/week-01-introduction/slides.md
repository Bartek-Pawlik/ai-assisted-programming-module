---
title: Module Introduction
week: 1
topic: introduction
type: lecture
source: authored
marp: true
theme: aiap
paginate: true
transition: fade
---

<!-- Speaker notes: ~0:30. Title slide while the room settles. This is a
two-act hour: logistics first (they need it today), then what the module
actually argues. Say the argument out loud early — most of them assume
this module is "how to use Copilot", and it is not. -->

<!-- _class: lead -->

<span class="kicker">// AI-Assisted Programming · Semester 1</span>

# Module Introduction

Atlantic Technological University

---

<!-- Speaker notes: ~2:00. The hook. Ask for hands: "who used an AI tool
to write code in the last week?" Nearly every hand goes up. Then the
second question, and far fewer hands stay up.

Do NOT resolve it here — it is answered deliberately three slides later
("So — must you understand every line?"), after the industry data has
made the honest answer defensible. Resolving it now costs the payoff.

The misconception to expect: the room reads the second question as an
accusation and assumes the expected answer is "you should be able to".
The real answer is no, almost nobody can, and the interesting question is
what replaced it. Let them sit in the discomfort for three slides. -->

## Two questions

* Who used an AI tool to write code in the last week?

* Who could **explain every line** it gave you?

<span class="kicker">// the gap between those two answers is this module</span>

---

<!-- Speaker notes: ~4:00. The thesis. The misconception to name out loud:
students expect a tools module ("learn Copilot, learn Cursor"). Tools
change every few months; the judgement does not. Say that the tool list in
week 13 will not match the tool list in week 1 — and that this is the
point, not a flaw. -->

## What this module is

* Not "how to use Copilot" — tools change every few months

* How to **direct** an AI assistant, and how to **judge** what comes back

- Prompting, retrieval, protocols, agents, deployment, review

<div class="callout">

**The uncomfortable part.** You are accountable for code you did not
write. The assistant is fast; your name is on the commit.

</div>

---

<!-- Speaker notes: ~5:00. THE stats slide — expect photographs, so pause.
Read the second and third numbers together and let the contradiction land
before saying anything: they don't trust it, and they ship it anyway.

The misconception to name: students assume professionals have solved this
and there is a correct process they are about to be taught. There isn't.
The industry is running an uncontrolled experiment and these are the
early results.

Provenance caveat, say it out loud: these come from 2026 industry surveys
of varying quality that recycle each other. Trust the DIRECTION, not the
decimal point. That scepticism is itself part of the module. -->

## Where this actually is, in 2026

| | |
|---|---|
| US developers using AI coding tools daily | **92%** |
| …who trust the code it produces | **29%** |
| …who always review it before committing | **48%** |
| Major issues vs human-written code | **1.7×** |
| AI samples with an OWASP Top-10 vulnerability | **~45%** |

<span class="kicker">// they don't trust it — and they ship it anyway</span>

---

<!-- Speaker notes: ~8:00. This resolves the opening question honestly,
and it is the intellectual spine of the hour. Do NOT let them leave with
"so reading code doesn't matter".

The misconception: students hear "nobody reads every line" as permission
to read none of it. The actual shift is that the UNIT of review moved —
from the line to the behaviour — and the guarantee moved from your eyes
to your tests. If you have no tests, you have not moved up a level; you
have just stopped checking.

Callback to the two questions at the start. -->

## So — must you understand every line?

* **No.** Almost nobody does, and pretending otherwise is dishonest

* But the review didn't disappear — it **moved**

- From *reading every line* → to *tests, types, and CI that must pass*
- From *"looks right"* → to *"prove it behaves right"*

<div class="callout">

**The trade only works if the verification is real.** Skip the tests and
you have not moved up a level — you have just stopped checking.

</div>

---

<!-- Speaker notes: ~11:00. Vocabulary slide. These are current terms
students will meet online and in interviews this year, and knowing them
is genuinely useful social capital — say that.

"Comprehension debt" is the one worth dwelling on: it is the technical-debt
argument applied to understanding rather than to code, and it reframes
speed as borrowing. Ask the room who has already inherited a haunted
codebase from their own past self. Most hands go up, AI or no AI. -->

## The words you'll hear this year

- **Vibe coding** — prompt it, run it, ship it, barely read it
- **Comprehension debt** — the future cost of understanding code a
  machine wrote and nobody read
- **Haunted codebase** — a working system the team no longer understands
- **Context engineering** — the shift from *how you ask* to *what you
  put in front of the model*
- **Spec-driven development** — the backlash: write the spec, let the
  agent implement it

<span class="kicker">// half of these did not exist two years ago</span>

---

<!-- Speaker notes: ~6:00. Agenda. Reference slide, immediate bullets, take
it at pace. Point at the two-act structure so they know logistics end and
content begins. -->

## This hour

- Act 1 — how the module runs: schedule, assessment, effort
- Act 2 — the tools you need set up before next week

---

<!-- Speaker notes: ~7:00. Schedule. The number that matters is 12 weeks,
not 13 — this changed from previous years. Reading week is the October
bank-holiday week and sits between weeks 6 and 7, right before MCQ 1. Say
explicitly that reading week is for revision, not a holiday from the
project. -->

## Duration and contact time

- **12 teaching weeks**, plus a reading week
- Reading week is the October bank-holiday week — it sits between week 6
  and MCQ 1
- Each week: **1 hour lecture + 2 hour lab**
- **No lab in week 1** — labs start next week
- The class is split into groups for labs; check your timetable

<span class="kicker">// timetables.atu.ie</span>

---

<!-- Speaker notes: ~10:00. Enrolment. Do this live — walk the room while
they enrol, it is faster than answering it by email for two weeks. The
group passwords are given out HERE, verbally, and are deliberately not in
this deck or the repo: the deck is published on a public website. -->

## Enrol on Moodle

1. Go to **vlegalwaymayo.atu.ie**
2. Search for course **10720** — *AI Assisted Programming*
3. Find out which group you are in (A, B or C)
4. Click **Enrol** and use your group's enrolment password

<div class="callout">

**Passwords are given out in this lecture**, not published. If you miss
them, email me — this deck is on a public site.

</div>

---

<!-- Speaker notes: ~13:00. Learning outcomes. Reference slide, read fast,
it is a validation requirement more than a teaching moment. Outcome 3 is
the one that actually drives the assessment design — flag it. -->

## Module learning outcomes

- **Identify and evaluate** AI-powered coding tools — generation,
  completion, debugging
- **Integrate** them into a real development workflow
- **Critically analyse** their limits: code quality, over-reliance, bias
- **Explore** emerging trends in the field

<span class="kicker">// outcome 3 is why the assessment looks the way it does</span>

---

<!-- Speaker notes: ~16:00. Assessment. THE slide of the hour — expect
photographs, pause here. The weighting changed this year: MCQs are 20%
each (down from 33%) and the project is 60%. Say the number twice. The
misconception to head off: "the project is at the end so I start it at the
end". It is 60% and it is due in week 12; people who start in week 10
fail it. -->

## Assessment

| Component | Weight | When |
|---|---|---|
| MCQ 1 | **20%** | Week 7, in the lab |
| MCQ 2 | **20%** | Week 12, in the lab |
| **Project** | **60%** | Due end of week 12 |

<div class="callout">

**The project is 60%.** The brief is published in week 2. Start it early —
not in week 10.

</div>

---

<!-- Speaker notes: ~20:00. How the MCQs work. Point out they are drawn
from lectures AND labs — students consistently revise only the slides and
are surprised by lab questions. The NotebookLM tip is genuinely good; also
point at the practice app on the module site, which is built from this
module's own material. -->

## The MCQs

* Multiple choice, sat **in person** in the lab slot

* Drawn from the lectures **and the labs** of previous weeks

- MCQ 1 covers weeks 1–6 · MCQ 2 covers weeks 8–11

**To practise:** use the practice app on the module site, or upload the
week's material to a tool like NotebookLM and ask it to generate questions.

---

<!-- Speaker notes: ~23:00. The project. Two hard requirements: it must
incorporate some AI technology, and it must follow the brief. Language is
their choice — say this clearly, people ask every year. The interesting
constraint is the defence: they present it, so they must understand it.
That is what makes a 60% project safe to hand to a cohort with AI tools. -->

## The project — 60%

- An application in **a language of your choice**
- Must incorporate **some AI technology** (image generation, an LLM
  feature, retrieval, a agentic workflow…)
- You **may** use AI tools to help build it — that is the point of the
  module
- You **will** present and defend it

<span class="kicker">// full brief published in week 2</span>

---

<!-- Speaker notes: ~26:00. Effort. Say the hours out loud: 5 credits is
100-125 hours across 12 weeks, which is roughly 8-10 hours a week
INCLUDING the 3 contact hours. So 5-7 hours of their own time weekly. Most
students underestimate this by half. -->

## Effort required

- A **5-credit** module — 100–125 hours of work
- Across 12 weeks, that is roughly **8–10 hours a week**, contact time
  included
- Self-directed learning is the main source of learning

<div class="callout">

Three of those hours are timetabled. The rest are yours to schedule.

</div>

---

<!-- Speaker notes: ~29:00. Act 2 begins — tools. This is the slide they
need to act on before next week's lab, so be concrete. The Student
Developer Pack is free and takes ten minutes; without it they hit paywalls
in week 4 onward. -->

## Tools you need

| Tool | What for |
|---|---|
| **GitHub** | Where your work lives |
| **Codespaces** | A full dev environment in the browser |
| **GitHub Copilot** | AI assistance inside the editor |
| **CLI coding agents** | Covered from week 8 |

<span class="kicker">// nothing to install — Codespaces runs in a browser</span>

---

<!-- Speaker notes: ~32:00. The to-do. Make them write these two down. The
username one sounds trivial and is not: they will be sending me repo links
all semester, and "xX_dark_slayer_Xx" makes marking genuinely harder. Also
it is the account they will show an employer. -->

## Before next week

* Sign up for the **GitHub Student Developer Pack** — it is free and
  unlocks Copilot

* Change your GitHub username to **your actual name**

<div class="callout">

Your GitHub account is the one an employer will look at. Start it as you
mean to continue.

</div>

---

<!-- Speaker notes: ~35:00. Where everything lives. Show the site live —
open it, click into a lab, show it works on a phone. Emphasise that the
site is canonical: if a lab is corrected mid-semester, the site has the
correction and their copy may not. -->

## Where everything lives

- **The module site** — every lecture, every lab, the project brief and
  MCQ practice, in a browser
- **Your own copy** — click *Use this template* to get a private
  repository for your lab work
- The site is always current. If a lab is corrected, it is corrected there
  first.

<span class="kicker">// danielcregg.is-a.dev/ai-assisted-programming</span>

---

<!-- Speaker notes: ~38:00. Summary and close. Return to the two questions
from the start — that symmetry is the point of the hour. Then: next week
is the overview lecture and the first lab, which is environment setup.
Leave time for questions. -->

## Summary

- **12 weeks**, 1 hour lecture + 2 hour lab, no lab this week
- **20% + 20% + 60%** — two MCQs and a project
- The project brief lands **next week**; start early
- Set up GitHub and the Student Developer Pack **before** next week

**The one idea to keep:** you don't have to read every line — but
something has to check it, and if that something isn't a test, it's you.

**Next week:** what AI-assisted programming actually is — and the first
lab.
