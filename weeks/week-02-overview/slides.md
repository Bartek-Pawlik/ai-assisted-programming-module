---
title: What AI-Assisted Programming Actually Is
week: 2
topic: overview
type: lecture
source: authored
marp: true
theme: aiap
paginate: true
transition: fade
---

<!-- Speaker notes: ~0:01. Title while they settle.

This hour has one job: give them a MODEL of what the tool is, accurate
enough to predict its behaviour. Everything afterwards depends on it. A
student who thinks the assistant "looks things up" will be confused by
hallucination for the whole semester; one who knows it predicts text will
find hallucination obvious. -->

<!-- _class: lead -->

<span class="kicker">// what is actually happening when it writes code</span>

# What AI-Assisted Programming Actually Is

---

<!-- Speaker notes: ~0:02. The hook. Put the completion up and ask what
happens next. Nearly everyone has seen this behaviour; almost nobody has
asked why it does it.

Do not answer yet — it is answered on the "prediction, not retrieval"
slide. The gap is the hour. -->

## A question you already know the answer to

You type a function name. It writes the body.

<!-- no-parse -->
```python
def calculate_median(numbers):
```

* How did it know?

* And why is it sometimes **confidently, fluently wrong**?

---

<!-- Speaker notes: ~0:04. THE idea of the hour, and the single most
useful sentence in it. Say it slowly.

The misconception this kills: students assume the tool SEARCHES — that it
has a database of code and finds the matching snippet. That model predicts
"it can only give me code that exists", which is wrong, and makes
hallucination inexplicable. Prediction explains both the magic and the
failures with one mechanism. -->

## The one idea

<div class="callout">

It is not looking anything up. It is **predicting the next token**, over
and over, based on everything it has seen so far.

</div>

* Astonishing output and confident nonsense come from the **same**
  mechanism

* Nothing in it checks whether the answer is true

---

<!-- Speaker notes: ~0:06. Agenda. Reference slide, immediate bullets,
brisk. -->

## This hour

- Prediction, not retrieval — and what follows from it
- The shapes these tools come in
- What they are genuinely good at
- Where they fail, and why those failures are predictable
- What the job becomes

---

<!-- Speaker notes: ~0:07. The mechanism, one slide, no more. Resist
teaching transformers — they do not need architecture, they need a
predictive model of behaviour.

The three consequences are the payload. Each one will be visible in their
own work within a fortnight. -->

## What follows from prediction

<div class="flow">
  <div class="step"><span class="n">01</span>Reads everything in its context</div>
  <div class="step"><span class="n">02</span>Predicts the most plausible next piece</div>
  <div class="step"><span class="n">03</span>Appends it, and repeats</div>
</div>

* **Plausible is the target** — not correct, not safe, not current

* It cannot tell you what it does not know, because it does not know that
  it does not know

- Change the context and you change the output. That is your entire
  steering wheel

---

<!-- Speaker notes: ~0:10. PREDICT beat 1. Give them 30 seconds and take
hands on each option before revealing.

The wrong answer to expect is (b), "it will say it doesn't know". Students
project honesty onto it, because a human expert who did not know would say
so. But "I don't know" is a rare continuation in training data compared
with a confident answer, so the plausible next token is a plausible-looking
function — which is exactly what you get.

This lands the hallucination idea by prediction rather than by assertion,
and they will meet it for real in the lab. -->

## Predict: what does it do?

You ask for a function using `pandas.read_excel_fast()`.

**That function does not exist.**

* It writes a function that calls it, confidently
* It tells you the function does not exist
* It refuses to answer
* It searches the internet to check

---

<!-- Speaker notes: ~0:13. The reveal. It writes the code — because a
confident continuation is more plausible than an admission of ignorance.

Then name it: hallucination. Tie it forward — this exact behaviour becomes
an attack surface later in the course when attackers register the invented
names. Do not elaborate; just plant it. -->

## It writes the code

<p class="prompt">Write a function that loads a spreadsheet using
pandas.read_excel_fast()</p>

<p class="reply">def load_sheet(path):
    return pd.read_excel_fast(path, engine="openpyxl")</p>

* Fluent. Well-named. Correctly styled. **Completely fictional.**

<div class="callout">

This is a **hallucination**, and it is not a bug being fixed — it is the
mechanism working exactly as designed.

</div>

---

<!-- Speaker notes: ~0:16. The shapes. This is the slide that ages
fastest, so teach the CATEGORIES and treat the named products as examples
that will change. Say that out loud — it is honest and it makes the slide
still useful in two years.

Reference slide: immediate bullets, brisk pace. -->

## The shapes these tools come in

| Shape | What it does | Where it lives |
|---|---|---|
| **Completion** | Finishes the line or block you are typing | Inline, as you type |
| **Chat** | Answers questions about code you show it | A side panel |
| **Edit** | Rewrites a selection you describe | In the file, as a diff |
| **Agent** | Works out the steps and does them | Editor or terminal |

<span class="kicker">// the products change yearly; the shapes have been stable</span>

---

<!-- Speaker notes: ~0:19. Genuinely good at. Be positive here and mean
it — a lecture that only warns gets discounted, and the room already knows
these tools are useful.

The unifying property is worth stating: everything on this list is a task
where the answer is CONVENTIONAL, and conventional is exactly what a
next-token predictor is best at. -->

## What they are genuinely good at

- Boilerplate you have written a hundred times
- Translating between languages or formats
- Explaining unfamiliar code, at speed
- First-draft tests, docstrings, regexes
- Naming things, and the mechanical half of refactoring

<div class="callout">

The pattern: tasks where the right answer is **conventional**. A predictor
of plausible text is excellent at what is, by definition, typical.

</div>

---

<!-- Speaker notes: ~0:22. The mirror image. Symmetry with the previous
slide is deliberate — same mechanism explains both columns, which is the
whole point of teaching prediction first.

The one that costs students most is the last: it does not know your
codebase unless you show it. Half of "the AI is useless here" complaints
are actually context problems. -->

## Where they fail, predictably

- Anything **novel** — if it is not typical, it is not plausible
- Anything **recent** — training has a cutoff, and libraries move
- **Your** conventions, unless you show them
- Arithmetic and counting, still
- Knowing when to stop: it will confidently answer a question you should
  not have asked

<span class="kicker">// every one of these follows from "plausible, not correct"</span>

---

<!-- Speaker notes: ~0:25. PREDICT beat 2. Show both, ask which gets the
better answer. Take a vote before revealing.

The wrong answer to expect is that they are equivalent — "it knows Python,
so it knows what a valid email is". The faulty model is that the tool has
one fixed level of competence. It does not: quality is a function of what
you put in front of it, and B supplies a decision the tool would otherwise
have to guess. This sets up context engineering directly. -->

## Predict: which gets the better answer?

<p class="prompt bad">Write a function to validate an email address</p>

<p class="prompt good">Write a function to validate an email address.
We accept anything with an @ and a dot after it — we deliberately do NOT
want RFC 5322 compliance. Reject anything over 254 characters.</p>

* Same tool. Same model. **Same day.**

---

<!-- Speaker notes: ~0:28. The reveal and the lesson. B wins, and not
because it is longer — because it makes a DECISION the tool would
otherwise make for you, silently and probably wrong.

Land this: the gap between those two answers is skill, and it is learnable.
That is the optimistic note of the hour and it is true. -->

## The second one, every time

* Not because it is longer — because it **decides** something

* Left unspecified, the tool picks for you, silently

<div class="callout">

Validation strictness is a **product decision**. Hand it to a text
predictor and you get whatever was most common in its training data.

</div>

- The gap between those two answers is **skill**, and skill is learnable

---

<!-- Speaker notes: ~0:31. What the job becomes. This reframes the whole
module and answers the anxious question in the room, which is usually
"does this replace me".

Answer it directly. The generation of code got cheap; deciding what should
exist and whether what arrived is right did not. That is the job, and it
is a more senior job than the one it replaced. -->

## So what is the job now?

<div class="stack">
  <div class="layer top"><span>Deciding what should exist, and what "correct" means</span><span class="rank">yours</span></div>
  <div class="layer"><span>Supplying the context that makes a good answer possible</span><span class="rank">yours</span></div>
  <div class="layer"><span>Judging what came back</span><span class="rank">yours</span></div>
  <div class="layer untrusted"><span>Typing the characters</span><span class="rank">cheap now</span></div>
</div>

* The bottom row got cheap. **The other three did not.**

---

<!-- Speaker notes: ~0:34. PREDICT beat 3, and the honest one. Ask for a
show of hands on each before revealing that the honest answer is "it
depends, and measured results are mixed".

The wrong answer to expect is a large single number — students have
absorbed "AI makes you 10x faster" from marketing. Controlled studies find
much smaller and highly task-dependent effects, and some find experienced
developers on familiar code get SLOWER while feeling faster. The
perception gap is the finding worth remembering. -->

## Predict: how much faster does this make you?

* 10× faster
* Roughly 2× faster
* It depends enormously on the task
* Sometimes **slower** — while feeling faster

---

<!-- Speaker notes: ~0:37. The honest answer. Both of the last two are
right, and the "feels faster than it is" result is the one that changes
behaviour.

Say plainly that headline productivity numbers in vendor material are
marketing. Measured effects are real but modest and task-dependent. This
buys enormous credibility for everything else you tell them. -->

## Honestly: it depends

- Large gains on **boilerplate and unfamiliar territory**
- Small or negative on **code you know well**
- Debugging is the hardest to measure and the easiest to lose time on

<div class="callout">

The uncomfortable finding: developers often report feeling faster on tasks
where measurement says they were not. **Perceived** speed and **actual**
speed come apart.

</div>

---

<!-- Speaker notes: ~0:40. Common mistakes. These are the five behaviours
that will cost them most this semester, in the order they will meet them.

The last is the important one — an assistant asked to solve a problem does
not stop to ask whether the problem is worth solving. -->

## Common mistakes

* Believing it **looked something up**

* Accepting the first answer because it is fluent

- Giving it a vague ask, then blaming the tool for guessing
- Not showing it the code it needs to see
- Letting it answer a question you should have questioned

---

<!-- Speaker notes: ~0:43. Summary and close. Return to the opening
completion — they can now answer both halves of the question themselves,
so ask THEM rather than restating it.

Leave the callout up for questions. -->

## Summary

- It **predicts plausible text**. It does not retrieve, and it does not
  verify
- Brilliance and hallucination are the **same mechanism**
- Four shapes — completion, chat, edit, agent — and the products change
  yearly
- Good at conventional, weak at novel, recent, or specific to you
- Quality is largely a function of **what you put in front of it**

<div class="callout">

The typing got cheap. Deciding what should exist, and judging what came
back, did not.

</div>
