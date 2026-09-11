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

<!-- Speaker notes: ~0:01. Title slide while the room settles. This is a
two-act hour: logistics first (they need it today), then what the module
actually argues. Say the argument out loud early — most of them assume
this module is "how to use Copilot", and it is not. -->

<!-- _class: lead -->

<span class="kicker">// AI-Assisted Programming</span>

# Module Introduction

---

<!-- Speaker notes: ~0:02. The hook. Ask for hands: "who used an AI tool
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

<!-- Speaker notes: ~0:04. The thesis. The misconception to name out loud:
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

<!-- Speaker notes: ~0:05. The load-bearing pair is rows two and three: 29%
trust the output and 48% always review it. Those two numbers together say
that the majority of developers ship code they do not trust and did not
check — not through carelessness, but because reviewing everything is no
longer possible at the rate it arrives. The rest of the table is the
consequence: 1.7x the major issues, ~45% carrying a known vulnerability
class.

The misconception is that professionals have solved this and there is a
correct process about to be taught. There is not. The faulty model is that
industry practice is settled and students are being inducted into it; in
fact this is an uncontrolled experiment in progress and these are early
results. A student who believes a solved process exists will look for the
rule instead of building the judgement.

Provenance matters as much as the figures: these are 2026 industry surveys
of varying rigour that recycle each other, so the direction is sound and
the precision is not. Deck weight: heavy, and it pays off the opening two
questions. Delivery: pause. -->

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

<!-- Speaker notes: ~0:08. This resolves the opening question honestly,
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

<!-- Speaker notes: ~0:11. Vocabulary slide. These are current terms
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

<!-- Speaker notes: ~0:06. Agenda. Reference slide, immediate bullets, take
it at pace. Point at the two-act structure so they know logistics end and
content begins. -->

## This hour

- Act 1 — how the module runs: schedule, assessment, effort
- Act 2 — the tools you need set up before next week

---

<!-- Speaker notes: ~0:07. Schedule. The number that matters is 12 weeks,
not 13 — this changed from previous years. Reading week is the October
bank-holiday week and sits between weeks 6 and 7, right before MCQ 1. Say
explicitly that reading week is for revision, not a holiday: MCQ 1 is
the week straight after it. -->

## Duration and contact time

- **12 teaching weeks**, plus a reading week
- Reading week is the October bank-holiday week — it sits between week 6
  and MCQ 1
- Each week: **2 hour lecture + 2 hour lab**
- **No lab in week 1** — labs start next week
- The class is split into groups for labs; check your timetable

<span class="kicker">// your lab group and room are on your timetable</span>

---

<!-- Speaker notes: ~0:10. Enrolment. Do this live — walk the room while
they enrol, it is faster than answering it by email for two weeks. The
group passwords are given out HERE, verbally, and are deliberately not in
this deck or the repo: the deck is published on a public website. -->

## Enrol on the VLE

1. Go to your college's **VLE** — the link is on your timetable
2. Search for **AI-Assisted Programming**
3. Find out which lab group you are in (A, B, C or D)
4. Click **Enrol** and use your group's enrolment password

<div class="callout">

**Passwords are given out in this lecture**, not published. If you miss
them, email me — this deck is on a public site.

</div>

---

<!-- Speaker notes: ~0:13. Learning outcomes. Reference slide, read fast,
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

<!-- Speaker notes: ~0:16. Assessment. THE slide of the hour — expect
photographs, pause here. The shape changed this year: there is no project.
Two in-person MCQs at 32% each, and nine small practical assessments at 4%
each, one per lab. The misconception to head off: "4% is nothing, I'll skip
the odd one". Nine of them are 36% of the module, and a skipped one counts
as zero — it is not dropped from the total. -->

## Assessment

| Component | Weight | When |
|---|---|---|
| MCQ 1 | **32%** | Week 7, in the lab |
| MCQ 2 | **32%** | Week 12, in the lab |
| Practical Assessments | **9 × 4%** | One per lab, open all that week |

<div class="callout">

**Nine small continuous assessments are 36% of the module.** A missed one counts as
zero, and each closes at the end of its week.

</div>

---

<!-- Speaker notes: ~0:20. How the MCQs work. Point out they are drawn
from lectures AND labs — students consistently revise only the slides and
are surprised by lab questions. The NotebookLM tip is genuinely good; also
point at the practice app on the module site, which is built from this
module's own material. -->

## The two MCQs

* Multiple choice, sat **in person** in the lab slot

* Drawn from the lectures **and the labs** of previous weeks

- MCQ 1 covers weeks 1–6 · MCQ 2 covers weeks 8–11

**To practise:** use the practice app on the module site, or upload the
week's material to a tool like NotebookLM and ask it to generate questions.

---

<!-- Speaker notes: ~0:23. The practical assessments. One short online
question per lab on the VLE, open Monday to Sunday of that lab's week, one attempt,
submitted automatically when the week closes. AI tools are allowed, as in
the labs. The misconception to head off: "if AI is allowed, I can paste the
question in". Each question is built so the question alone is not enough —
it asks about the lab code in front of them, what it actually does when
run, or what is true right now. Doing the lab is the preparation. -->

## The Practical Assessments (PAs)

- **One per lab**, on the VLE, worth **4%** each
- Open **all week** — do it when it suits you, not only in the lab
- You **may** use AI tools, as you do in the labs
- But the question alone is not enough: each asks about **the lab code in
  front of you** and what it actually does

<span class="kicker">// the first one opens with the first lab</span>

---

<!-- Speaker notes: ~0:29. Act 2 begins — tools. This is the slide they
need to act on before next week's lab, so be concrete. The Student
Developer Pack is free and takes ten minutes; without it they hit paywalls
in week 4 onward. -->

## Tools you need

| Tool | What for |
|---|---|
| **GitHub** | Where your work lives |
| **Codespaces** | A full dev environment in the browser |
| **GitHub Copilot** | AI assistance inside the editor |
| **CLI coding agents** | Covered in week 9 |

<span class="kicker">// nothing to install — Codespaces runs in a browser</span>

---

<!-- Speaker notes: ~0:32. The to-do. Make them write these two down. The
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

<!-- Speaker notes: ~0:35. Where everything lives. Show the site live —
open it, click into a lab, show it works on a phone. Emphasise that the
site is canonical: if a lab is corrected mid-semester, the site has the
correction and their copy may not. -->

## Where everything lives

- **The module site** — every lecture, every lab and the MCQ practice, in
  a browser
<div style="text-align: center; font-size: 1.5em;">
  <a href="http://danielcregg.is-a.dev/ai-assisted-programming">http://danielcregg.is-a.dev/ai-assisted-programming</a>
</div>
<br>

- **Your own copy** — click *Use this template* to get a private
  repository for your lab work


<div style="text-align: center; font-size: 1.5em;">
  <a href="https://github.com/danielcregg/ai-assisted-programming">https://github.com/danielcregg/ai-assisted-programming</a>
</div>
<br>

---

<!-- Speaker notes: ~0:38. Summary and close. Return to the two questions
from the start — that symmetry is the point of the hour. Then: next week
is the overview lecture and the first lab, which is environment setup.
Leave time for questions. -->

## Summary

- **12 weeks**, 2 hour lecture + 2 hour lab, no lab this week
- **32% + 32% + 9 × 4%** — two MCQs and nine practical assessments
- The first practical assessment opens **next week**, with the first lab
- Set up GitHub and the Student Developer Pack **before** next week

**The one idea to keep:** you don't have to read every line — but
something has to check it, and if that something isn't a test, it's you.

**Next week:** what AI-assisted programming actually is — and the first
lab.
