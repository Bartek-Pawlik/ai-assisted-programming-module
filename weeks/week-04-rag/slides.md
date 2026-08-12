---
title: Retrieval and Grounding
week: 4
topic: rag
type: lecture
source: authored
marp: true
theme: aiap
paginate: true
transition: fade
---

<!-- Speaker notes: ~0:01. Title while they settle.

The framing of this hour is deliberately different from the usual RAG
lecture. Most teach the pipeline and stop. This one teaches the DECISION
first — retrieve or don't — because building infrastructure a problem does
not need is a commoner and costlier mistake than the reverse. -->

<!-- _class: lead -->

<span class="kicker">// giving it what it does not know</span>

# Retrieval and Grounding

---

<!-- Speaker notes: ~0:02. The hook. Ask it straight and take hands.

Almost everyone assumes the model must be TAUGHT the document — retrained
or fine-tuned. That instinct is the thing to dislodge, and it dissolves
the moment they remember the context window. Do not reveal yet. -->

## A problem you cannot prompt your way out of

Your company has 40,000 internal documents.

A user asks a question whose answer is in one of them.

* The model has never seen any of them

* How do you get it to answer **correctly**?

---

<!-- Speaker notes: ~0:04. The idea. Say it slowly — it is the whole hour
in one sentence, and it reframes the problem from "teach the model" to
"put the right text in front of it".

The misconception this kills: that answering from private data requires
training. It does not. Training is expensive, slow, and does not update.
Retrieval is cheap, instant, and always current. -->

## The one idea

<div class="callout">

You do not teach the model your documents. You **find the relevant piece
and put it in the prompt.**

</div>

* No retraining. No fine-tuning

* The model is the reasoning engine; **you** supply the facts

---

<!-- Speaker notes: ~0:05. Agenda. Brisk. Flag section 1 as the one that
distinguishes this from the version of this lecture taught last year. -->

## This hour

- **Do you even need retrieval?** — the decision first
- How retrieval works: chunk, embed, search
- Why embeddings beat keyword search
- Grounding, citation, and what it fixes
- Where it goes wrong

---

<!-- Speaker notes: ~0:07. The decision, and the part most RAG lectures
skip entirely.

The history matters: when RAG became popular, context windows held a few
thousand tokens. Retrieval was the ONLY way to work with a large document.
Windows are now hundreds of thousands to millions of tokens, so for many
problems you can simply paste the whole thing. -->

## First: do you need it at all?

* When RAG became popular, context windows held a **few thousand** tokens

* Retrieval was the only way to work with anything larger

- Today's windows hold **hundreds of thousands** to millions

<div class="callout">

For a lot of problems, the correct architecture is now **paste the whole
thing in.** No chunking, no embeddings, no database to maintain.

</div>

---

<!-- Speaker notes: ~0:09. PREDICT beat 1. Take a vote before revealing.

The wrong answer to expect is "build the RAG pipeline" — students have
been told RAG is what you do with documents, so they reach for it
reflexively. Five documents of a few thousand words fit comfortably in a
modern window, and retrieval can only LOSE information a full read would
have had. The faulty model is that RAG is a best practice rather than a
trade-off against a constraint that has largely lifted. -->

## Predict: five short documents, conversational questions

You have five documents, a few thousand words in total. Users ask open
questions about them.

* Chunk, embed, and build a vector database
* Paste all five into the prompt
* Fine-tune a model on them
* Summarise each, then discard the originals

---

<!-- Speaker notes: ~0:12. The reveal, then the decision table — the
slide to photograph.

Be explicit that this is a trade-off table, not a ranking. The cost
crossover around a couple of thousand pages is worth quoting because it
gives them a number to reason with rather than a vibe. -->

## It depends — and here is on what

| Situation | Reach for |
|---|---|
| Small corpus, conversational questions | **Long context** — just paste it |
| Too large to fit, or thousands of documents | **Retrieval** |
| You must cite which source said it | **Retrieval** |
| Data changes constantly | **Retrieval**, or live search |
| Cost matters at scale | **Retrieval** — crossover ≈ a couple of thousand pages |

---

<!-- Speaker notes: ~0:14. The honest limits of the "just paste it"
answer, so they do not leave with the opposite oversimplification.

"Lost in the middle" is the memorable one: models attend less reliably to
material in the middle of a very long context than at either end. Adding
marginally relevant text can make an answer WORSE. More tokens is not more
understanding. -->

## Long context is not free either

- **Lost in the middle** — attention is less reliable in the middle of a
  very long input than at either end
- **Dilution** — marginally relevant text competes with the relevant part
- Cost and latency scale with everything you send

<div class="callout">

Adding more context can make an answer **worse**. More tokens is not more
understanding.

</div>

---

<!-- Speaker notes: ~0:17. Now the pipeline, having earned it. Keep it to
one slide of shape — the detail is the lab's job.

Emphasise that only step 5 involves the model at all. Steps 1-4 are
ordinary information retrieval, and that is why RAG is mostly a search
problem wearing an AI hat. -->

## How retrieval works

<div class="flow">
  <div class="step"><span class="n">01</span>Split documents into chunks</div>
  <div class="step"><span class="n">02</span>Embed each chunk as a vector</div>
  <div class="step"><span class="n">03</span>Embed the question too</div>
  <div class="step"><span class="n">04</span>Find the nearest chunks</div>
  <div class="step"><span class="n">05</span>Put them in the prompt</div>
</div>

* Only the **last** step involves the model

* Steps 1–4 are ordinary information retrieval

---

<!-- Speaker notes: ~0:19. Embeddings. The intuition only — no maths.

The one thing they must take away: an embedding puts MEANING in space, so
"car" and "automobile" land near each other even though they share no
letters. That is what keyword search cannot do and why this works. -->

## Embeddings: meaning as coordinates

* A vector of numbers representing **what a piece of text means**

* Similar meanings land **near each other**, whatever words they used

| Query | Keyword search finds | Embedding search finds |
|---|---|---|
| "car maintenance" | documents containing "car" | "vehicle servicing", "auto repair" |
| "how do I quit" | "quit" | "resignation process", "leaving the company" |

---

<!-- Speaker notes: ~0:22. PREDICT beat 2. This one is about chunk size,
and it is the parameter students get wrong most often in the lab.

The wrong answer to expect is "smaller chunks are more precise, so
smaller is better". The faulty model treats retrieval as lookup. In fact a
chunk that is too small loses the context that makes it meaningful — a
sentence saying "it must be replaced every 12 months" is useless when you
cannot tell what "it" is. Too large and you dilute. There is a middle, and
finding it is empirical. -->

## Predict: which chunk size retrieves best?

You split a manual into chunks. Which works best?

* One sentence per chunk — maximum precision
* One paragraph per chunk
* One page per chunk
* The whole document as one chunk

---

<!-- Speaker notes: ~0:25. The reveal: roughly a paragraph, and more
importantly WHY both extremes fail.

The pronoun example is the one that sticks — read it out. Then the honest
engineering point: there is no universally correct chunk size, it depends
on the documents, and the only way to know is to measure. That sets up
the lab's experiments. -->

## A paragraph, usually — and here is why

* **Too small:** *"It must be replaced every 12 months."* Replaced —
  what? The chunk lost its own subject

* **Too large:** one relevant sentence arrives with a page of noise

- Overlap between chunks stops a fact being split down the middle

<div class="callout">

There is no universally correct chunk size. It depends on your documents,
and the only way to know is to **measure**.

</div>

---

<!-- Speaker notes: ~0:27. Grounding — the payoff, and the reason RAG is
worth the trouble even where long context would also work.

Two properties: the answer is anchored to supplied text, and you can SHOW
which text. Citation is the one enterprises actually buy. -->

## Grounding

* The answer is anchored to text you supplied, not to what the model
  half-remembers

* You can **show which text** — the citation

<p class="prompt">Answer using ONLY the context below. If the context does
not contain the answer, say "I don't know".
&#10;
Context: {retrieved chunks}
Question: {question}</p>

---

<!-- Speaker notes: ~0:30. PREDICT beat 3, and the honest one. Vote
before revealing.

The wrong answer to expect is "yes, RAG fixes hallucination" — it is the
claim every vendor makes. It reduces it substantially and does not
eliminate it: the model can still misread a retrieved chunk, blend two
chunks, or fall back on training data when retrieval returns nothing
useful. "I don't know" is a rare continuation, so it needs explicit
permission — which is why the instruction on the previous slide says it
out loud. -->

## Predict: does retrieval eliminate hallucination?

* Yes — the answer comes from real documents now
* No, but it reduces it a lot
* No difference
* It makes it worse

---

<!-- Speaker notes: ~0:33. The reveal and the failure modes. Be specific
— vague warnings do not change behaviour.

The last one is the important one: if retrieval returns nothing useful and
you did not give explicit permission to say "I don't know", the most
plausible continuation is a confident answer from training data. -->

## It reduces it. It does not remove it.

- It can **misread** a retrieved chunk
- It can **blend** two chunks into a claim neither made
- If retrieval returns nothing useful, it may answer from training anyway

<div class="callout">

"I don't know" is a rare continuation in training data. If you want it,
you have to **explicitly permit it** — and then check that it does.

</div>

---

<!-- Speaker notes: ~0:35. Where it goes wrong in practice — the
operational failures, distinct from the model failures above.

Retrieval quality is the one that surprises people: if step 4 returns the
wrong chunks, everything downstream is confidently wrong and the system
looks like a model problem when it is a search problem. -->

## Where it goes wrong

| Failure | Symptom |
|---|---|
| Bad retrieval | Confident answers from irrelevant chunks |
| Chunks too small | Fragments with no context |
| Stale index | Correct answers to last month's question |
| No citation | Nobody can check anything |
| Everything embedded | Slow, expensive, no better |

<span class="kicker">// most "the AI is wrong" reports here are search bugs</span>

---

<!-- Speaker notes: ~0:38. The 2026 shape. Worth saying explicitly
because it resolves the false either/or the hour opened with.

Also worth naming agentic retrieval: their coding assistant does not
maintain a vector database of their repo — it greps and reads files on
demand. Same problem, solved with search instead of embeddings. -->

## What most real systems do now

<div class="flow">
  <div class="step"><span class="n">01</span>Retrieve a generous, bounded set</div>
  <div class="step"><span class="n">02</span>Let a long-context model read all of it</div>
  <div class="step"><span class="n">03</span>Answer with citations</div>
</div>

* Hybrid, not either/or

<div class="callout">

**Agentic retrieval:** your coding assistant does not embed your repo — it
*greps and reads files on demand.* Same problem, solved with search.

</div>

---

<!-- Speaker notes: ~0:41. Common mistakes. The first is the one this
whole hour is arranged to prevent.

The last one deserves a beat: an evaluation set of questions with known
answers is the difference between engineering and guessing, and almost
nobody builds one. -->

## Common mistakes

* Building a pipeline for a corpus that would **fit in the prompt**

* Blaming the model when retrieval returned the wrong chunks

- Chunking without ever measuring whether the size works
- Forgetting the index goes stale
- Having no set of questions with known answers to test against

---

<!-- Speaker notes: ~0:44. Summary and close. Return to the opening
problem — 40,000 documents — and note they can now answer it, including
the part where they check whether 40,000 is really the number.

Leave the callout up for questions. -->

## Summary

- You do not teach the model your data — you **put the right piece in the
  prompt**
- **Ask first whether you need retrieval.** Small corpus, conversational
  use → long context wins
- Retrieval earns its place on **scale, cost, freshness, citation**
- Chunk ≈ a paragraph, with overlap, and **measure** it
- Grounding reduces hallucination; it does not remove it

<div class="callout">

Building infrastructure a problem does not need is a commoner and more
expensive mistake than the reverse.

</div>
