---
title: Automated Checking and Evals
week: 10
topic: cicd
type: lecture
source: authored
marp: true
theme: aiap
paginate: true
transition: fade
---

<!-- Speaker notes: ~0:01. Title while they settle.

Two halves that are really one idea: automated checks for code that
behaves the same every time, and automated checks for code that does not.
The second half is the one nobody teaches and the one their project needs. -->

<!-- _class: lead -->

<span class="kicker">// making the machine check the machine</span>

# Automated Checking and Evals

---

<!-- Speaker notes: ~0:02. The hook. It follows directly from the argument
that you cannot read every line of generated code.

Ask it and let it sit. If review moved from your eyes to your tests, then
the tests are now load-bearing — and nobody checked whether they are any
good. Do not resolve yet. -->

## If you are not reading every line

…then something else is checking it.

* What, exactly?

* And who checks **that**?

---

<!-- Speaker notes: ~0:04. The idea. Say it once.

The misconception: students treat CI as an administrative hurdle imposed
by lecturers or employers. It is the opposite — it is the thing that makes
generating code you did not read a defensible engineering practice rather
than negligence. -->

## The one idea

<div class="callout">

Automated checks are what make it **defensible** to ship code you did not
read line by line. Without them you did not move up a level — you stopped
checking.

</div>

* CI is not administration. It is the other half of the trade

---

<!-- Speaker notes: ~0:05. Agenda. Flag the second half — evals — as the
part most people have never met. -->

## This hour

- What a pipeline actually is
- What to put in one, in order of value
- AI inside the pipeline
- **Evals** — checking things that answer differently every time
- LLM-as-judge, and its failure modes

---

<!-- Speaker notes: ~0:07. What a pipeline is. Deliberately unglamorous —
it is a script that runs on a trigger, and that is genuinely all it is.

The only real distinction from running it yourself: it runs whether or not
you remembered. -->

## A pipeline is a script with a trigger

<div class="flow">
  <div class="step"><span class="n">01</span>You push</div>
  <div class="step"><span class="n">02</span>A clean machine appears</div>
  <div class="step"><span class="n">03</span>It runs your checks</div>
  <div class="step"><span class="n">04</span>Pass or fail, visibly</div>
</div>

* The only real difference from running them yourself: **it runs whether
  or not you remembered**

---

<!-- Speaker notes: ~0:09. What to put in it, in value order. This is the
practical slide for their project.

The ordering is the teaching: linting is cheap and catches least; tests
cost most to write and catch most. Secret scanning is free and catches the
thing that ends careers. -->

## What goes in, roughly in value order

| Check | Cost to add | Catches |
|---|---|---|
| Does it build / import | Minutes | Broken merges |
| Linting and formatting | Minutes | Style drift, some bugs |
| Secret scanning | Minutes | The mistake you cannot undo |
| Dependency scanning | Minutes | Known vulnerabilities |
| Unit tests | Real effort | Actual regressions |

<span class="kicker">// the top four are nearly free; do them first</span>

---

<!-- Speaker notes: ~0:12. PREDICT beat 1. Vote before revealing.

The wrong answer to expect is "a full test suite" — students think CI
means tests, so they conclude a project without good tests gets nothing
from CI. In fact the highest value per minute is secret scanning: it costs
nothing to enable and catches the one failure that cannot be undone by
fixing the code. -->

## Predict: your project has few tests. What is worth adding first?

* Nothing — CI is pointless without a test suite
* A full test suite, before anything else
* Secret scanning and dependency checks
* A deployment step

---

<!-- Speaker notes: ~0:14. The reveal, with the asymmetry stated plainly.

A failing test costs you a red build. A leaked key costs you a rotation,
possibly a bill, possibly a breach — and pushing a fix does not un-leak
it. Irreversibility is what makes it top of the list. -->

## The checks you cannot undo by fixing the code

* A failing test → a red build. Push a fix

* A leaked key → rotate it, and hope. **Pushing a fix does not un-leak it**

<div class="callout">

Order your checks by **irreversibility**, not by sophistication.

</div>

---

<!-- Speaker notes: ~0:17. AI inside the pipeline. Short section — the
useful framing is what AI can check that a compiler cannot.

A linter finds style. A compiler finds type errors. Neither can say "this
function's name no longer matches what it does". -->

## AI inside the pipeline

- **Review on pull requests** — asks the questions a linter cannot
- **Issue triage** — classify, label, route
- **Documentation drift** — does the README still describe this code?

<div class="callout">

Ask it what a compiler **cannot** check. Never ask it whether the code
compiles — a compiler answers that exactly, and a model guesses.

</div>

---

<!-- Speaker notes: ~0:19. The honesty rule for AI in CI, and it is
worth a slide because it is a real failure mode.

If a model call fails, that is a FAILURE. It must not be written into the
report as though it were a finding, and a run that reviewed nothing must
go red rather than filing a cheerful empty report. Otherwise green stops
meaning anything. -->

## A failed call is a failure, not a finding

* If the model call errors, the run **failed**. It did not "find nothing"

* A job that reviewed nothing must go **red**

<div class="callout">

Otherwise you get the worst outcome available: a green tick over a check
that never ran.

</div>

---

<!-- Speaker notes: ~0:22. The turn into evals. This is where the hour
changes gear.

Set it up with the concrete problem: their project has an AI feature.
Every testing instinct they have assumes determinism. Same input, same
output, assertEqual. That assumption is now false. -->

## The turn: your project has an AI feature

* Same input. **Different output.** Every time

* Every testing instinct you have assumes determinism

<p class="prompt bad">assert summarise(article) == "Revenue grew 12%."</p>

* This test fails on a perfectly good answer

---

<!-- Speaker notes: ~0:24. The idea of evals. One sentence.

The shift from a test to a test SET, and from pass/fail to a rate, is the
whole concept. Everything else is technique. -->

## Evals: measure a rate, not a result

<div class="callout">

Stop asking "did this one call work?" Start asking **"across a set of
cases, how often is it acceptable — and is that number moving?"**

</div>

* One case tells you almost nothing

* Twenty cases tell you whether your change helped

---

<!-- Speaker notes: ~0:27. The assertion ladder. THE practical slide of
the second half — put it up and leave it.

Work down it: use the strongest assertion the task allows. Most teams jump
straight to LLM-as-judge when a structural check would have been exact,
cheap and deterministic. -->

## The assertion ladder

| Rung | Check | Use when |
|---|---|---|
| **Exact match** | `output == expected` | Classification, extraction |
| **Contains / regex** | Key fact present | The answer must mention something |
| **Structural** | Valid JSON, required fields | The output feeds other code |
| **Property** | Length, no leaked prompt, cites a source | Always worth adding |
| **LLM-as-judge** | Another model scores it | Nothing above can express it |

* Use the **strongest rung the task allows**, not the fanciest

---

<!-- Speaker notes: ~0:29. PREDICT beat 2. Vote before revealing.

The wrong answer to expect is "LLM-as-judge, because summaries are
subjective". The faulty model is that subjective output requires
subjective checking. Several exact, deterministic properties are available
here — mentions the figure, does not exceed a length, is not empty, does
not echo the prompt — and each is cheap and reliable. Judge is a last
resort, not a first. -->

## Predict: how do you test a summariser?

Your feature summarises articles. Which do you build first?

* LLM-as-judge — summaries are subjective
* Exact match against a reference summary
* Property checks: mentions the key figure, under 50 words, non-empty
* You cannot test it; ship and see

---

<!-- Speaker notes: ~0:32. The reveal. Property checks first — cheap,
deterministic, and they catch the failures that actually happen (empty
output, prompt echo, runaway length).

Then the honest note: judge is for the residue, the part properties cannot
express. -->

## Properties first, judge last

* Property checks are **cheap, deterministic and repeatable**

* They catch the failures that actually happen: empty output, prompt echo,
  runaway length, missing the key fact

- Keep the judge for the residue that no property can express

---

<!-- Speaker notes: ~0:34. LLM-as-judge and its failure modes. Be honest
— it is genuinely useful and genuinely biased.

Self-preference is the one to name: a model scoring output from the same
family tends to rate it higher. Position bias too: in an A/B comparison,
order affects the verdict. Both are measurable, both are real. -->

## LLM-as-judge, honestly

* Give a model the output and a rubric; ask for a score and a reason

* It works. It is also **biased in known ways**:

| Bias | What happens |
|---|---|
| Self-preference | Rates output from its own family higher |
| Position | In an A/B comparison, order changes the verdict |
| Verbosity | Longer answers score better than they deserve |

- Always ask for the **reason**, not just the score — an unjustifiable
  score is usually visibly unjustifiable

---

<!-- Speaker notes: ~0:37. PREDICT beat 3, and the one that most changes
their behaviour on the project.

The wrong answer to expect is "it got better — I improved the prompt and
the examples I checked all improved". That is exactly the trap: people
tune against the two or three cases they happen to look at, and regress
the ones they do not. Without a set measured before and after, "better" is
a feeling. -->

## Predict: you tweak the prompt and your three test cases improve

Is the feature better?

* Yes — the evidence is right there
* Unknown, until you measure the whole set
* Only if the model version stayed the same
* Yes, if the three cases were representative

---

<!-- Speaker notes: ~0:39. The reveal, and the regression point that
makes evals worth the effort at all.

This is the entire argument: without a measured set, prompt tuning is
folklore. With one, it is engineering. Say that. -->

## Unknown — and this is the whole point

* You improved the cases you were looking at

* You have no idea what happened to the ones you were not

<div class="callout">

Without a measured set, prompt tuning is **folklore**. With one, it is
engineering.

</div>

- Run the set on every change. Track the number over time

---

<!-- Speaker notes: ~0:42. Practical shape for their project. Keep it
small and achievable — 20 cases in a JSON file is a real eval suite and
takes an afternoon.

Discourage the instinct to build a framework. -->

## What this looks like for a project

<div class="flow">
  <div class="step"><span class="n">01</span>20 real inputs in a file</div>
  <div class="step"><span class="n">02</span>Expected properties per case</div>
  <div class="step"><span class="n">03</span>A script that scores the set</div>
  <div class="step"><span class="n">04</span>Run it in CI, record the rate</div>
</div>

* Twenty cases in a JSON file is a **real** eval suite

* Do not build a framework. Build the file

---

<!-- Speaker notes: ~0:44. Common mistakes. Mixed across both halves of
the hour. -->

## Common mistakes

* Treating CI as administration rather than as the other half of the trade

* Testing a non-deterministic feature with `assertEqual`

- Reaching for LLM-as-judge when a property check would be exact
- Tuning a prompt against the two examples you happened to look at
- Letting a failed model call be reported as "no findings"

---

<!-- Speaker notes: ~0:46. Summary and close. Return to the opening
question — "what is checking it, and who checks that?" — and let them
answer both halves.

Leave the callout up for questions. -->

## Summary

- Automated checks are what make **not reading every line** defensible
- Order checks by **irreversibility** — secret scanning before test suites
- Ask AI what a compiler **cannot** check, and treat a failed call as a
  failure
- Non-deterministic features need a **set** and a **rate**, not an assertion
- Climb the assertion ladder: **properties first, judge last**
- Measure before and after, or "better" is a feeling

<div class="callout">

Twenty cases in a file, scored on every change. That is the difference
between engineering and folklore.

</div>
