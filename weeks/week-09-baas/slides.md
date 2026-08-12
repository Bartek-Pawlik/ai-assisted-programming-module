---
title: Backend as a Service
week: 9
topic: baas
type: lecture
source: authored
marp: true
theme: aiap
paginate: true
transition: fade
---

<!-- Speaker notes: ~0:01. Title while they settle.

This hour sits slightly apart from the rest of the course: it is not about
AI. It is here because an assistant can now produce a convincing frontend
in minutes, and that frontend needs somewhere to put data. The gap between
"looks like an app" and "is an app" is the backend. -->

<!-- _class: lead -->

<span class="kicker">// where the data actually lives</span>

# Backend as a Service

---

<!-- Speaker notes: ~0:02. The hook. This is a situation most of them have
already been in, so ask for hands.

An assistant builds you a beautiful task app in ten minutes. Refresh the
page. Everything is gone. That gap is the hour. -->

## Ten minutes, one prompt, a working app

An assistant builds you a task list. It looks right. It works.

* You refresh the page

* Everything is gone

---

<!-- Speaker notes: ~0:04. The idea. Say it plainly.

The misconception: students conflate "the UI works" with "the app works".
An AI-generated frontend is genuinely impressive and genuinely stateless.
Persistence, identity and access control are the parts nobody prompts for
because nobody sees them. -->

## The one idea

<div class="callout">

An assistant will happily build you a **frontend**. It will not, unasked,
build you somewhere to **keep the data** — or decide who may read it.

</div>

* Persistence, identity and access control are invisible in a screenshot

* Which is exactly why they get skipped

---

<!-- Speaker notes: ~0:05. Agenda. Brisk. -->

## This hour

- What a backend actually has to do
- What BaaS gives you, and what it takes
- Data modelling when there are no joins
- Security rules — the part that bites
- Choosing: BaaS or your own backend

---

<!-- Speaker notes: ~0:07. What a backend does. Five jobs, and the point
is that all five exist whether or not you write them.

Students think "backend" means "the code I write". It means these five
responsibilities existing somewhere. -->

## Five jobs, whoever does them

<div class="stack">
  <div class="layer top"><span>Store data so it survives a refresh</span><span class="rank">persistence</span></div>
  <div class="layer"><span>Know who the user is</span><span class="rank">identity</span></div>
  <div class="layer"><span>Decide what they may see and change</span><span class="rank">authorisation</span></div>
  <div class="layer"><span>Run logic you cannot trust a browser with</span><span class="rank">server logic</span></div>
  <div class="layer"><span>Stay up, scale, get backed up</span><span class="rank">operations</span></div>
</div>

* These exist whether or not you write them

---

<!-- Speaker notes: ~0:10. What BaaS is. One line, then the trade.

The honest framing: you are renting all five responsibilities. That is a
genuinely good deal for a student project or an early product, and a real
commitment you should make with your eyes open. -->

## BaaS: renting all five

| You get | You give up |
|---|---|
| A database with an API, instantly | Control of the data layer |
| Auth: email, Google, GitHub | Portability — it is their SDK |
| Hosting and scaling | Predictable cost at scale |
| Client libraries | Some flexibility in modelling |

<span class="kicker">// Firebase, Supabase, Appwrite, Pocketbase — same shape</span>

---

<!-- Speaker notes: ~0:12. PREDICT beat 1, and the one that most changes
their project. Vote before revealing.

The wrong answer to expect is "the frontend talks to the database, that's
the point of BaaS". Students see the client SDK and conclude the browser
is trusted. It is not: anyone can open dev tools, read your config, and
call the same API with their own values. The config is public by design. -->

## Predict: where do the database credentials live?

Your BaaS-backed app runs entirely in the browser.

* On the server, safely hidden
* In the frontend code, where anyone can read them
* Encrypted in the browser
* Nowhere — the SDK handles it invisibly

---

<!-- Speaker notes: ~0:15. The reveal, and it genuinely surprises people.

The config IS public. It is not a secret and was never meant to be. Which
raises the obvious question — what stops a stranger reading your whole
database? — and that is the next slide. Let the question hang. -->

## In the frontend. Publicly.

* Your BaaS config ships in the client bundle. **It is not a secret**

* Anyone can read it, and call the same API with their own values

<div class="callout">

So what stops a stranger reading your entire database?

</div>

---

<!-- Speaker notes: ~0:17. Security rules — the answer, and the most
important slide in the hour.

The model: the database itself enforces access, per request, regardless of
who is asking or what client they used. Not the frontend. The frontend
cannot be trusted and is not being trusted. -->

## Security rules are the backend

* The **database** decides, on every request, what this user may do

* Not your frontend. Your frontend is not trusted and never was

```text
allow read:   if request.auth != null
              && resource.data.owner == request.auth.uid;
allow write:  if request.auth != null
              && request.resource.data.owner == request.auth.uid;
```

* This is the authorisation layer. It is **the** thing to get right

---

<!-- Speaker notes: ~0:20. PREDICT beat 2. Vote before revealing.

The wrong answer to expect is "it works fine, that's how you develop".
Open rules are the default in most tutorials and in most AI-generated
setups, and they are also how student projects leak. The faulty model is
that an obscure URL is a form of protection. It is not — these endpoints
get scanned. -->

## Predict: you ship with `allow read, write: if true`

You left the permissive development rule in place. Your app works
perfectly. What happens?

* Nothing — nobody knows your project URL
* Anyone who finds the config can read and delete everything
* The provider blocks it automatically
* Only logged-in users can access it

---

<!-- Speaker notes: ~0:23. The reveal. Open rules mean an open database,
and these endpoints are actively scanned.

Then the practical instruction: an assistant that scaffolds BaaS for you
will very often leave open rules in place, because that is what makes the
tutorial work. Check them. This is the concrete link back to the security
material. -->

## Anyone. Everything.

* These endpoints are scanned. Obscurity is not a control

<div class="callout">

An assistant scaffolding BaaS will very often leave **open rules** in
place — they are what makes the example work. Check them yourself, every
time.

</div>

- "It works" and "it is safe" are different tests, and only one of them is
  automatic

---

<!-- Speaker notes: ~0:26. Data modelling. The genuinely different skill,
and where relational habits hurt.

Document stores have no joins. So you model around the QUERIES you need
rather than around normalised truth, and duplication stops being a sin. -->

## Modelling without joins

* Document stores have **no joins**. You cannot assemble data at read time

* So you model around the **queries you need**, not around normal forms

| Relational instinct | Document store |
|---|---|
| Normalise, join at read | Duplicate what you read together |
| One source of truth | Update in several places |
| Schema enforced by the DB | Schema enforced by you |

---

<!-- Speaker notes: ~0:28. The duplication trade, stated honestly so it
does not read as sloppiness.

Storage is cheap; a read that needs three round trips is not. But the cost
is real: duplicated data must be updated everywhere, and nothing in the
database will remind you. -->

## Duplication is a trade, not a mistake

* Storage is cheap. A screen that needs three round trips is not

* But duplicated data must be updated **everywhere**, and nothing reminds
  you

<div class="callout">

Denormalise deliberately, and write down where each copy lives. The
database will not tell you when they disagree.

</div>

---

<!-- Speaker notes: ~0:31. Real-time. Brief — it is the genuinely
delightful feature and it demos well, but it is not the hour's spine.

Worth noting the cost: a listener is an open connection, and listeners on
large collections are the commonest surprise-bill story. -->

## Real-time, nearly free

* Subscribe to a query; the client is pushed changes as they happen

* Multi-user apps that would be a project on their own become a few lines

- The cost: an open connection per listener, and a listener on a large
  collection is the classic surprise bill

---

<!-- Speaker notes: ~0:33. PREDICT beat 3 — the cost model, which nobody
reads until it hurts.

The wrong answer to expect is "storage" — students model database cost as
disk, because that is how they think about files. BaaS pricing is
overwhelmingly per OPERATION. A page that reads a whole collection to show
a count is cheap once and ruinous at scale. -->

## Predict: what dominates a BaaS bill?

* The amount of data stored
* The number of reads and writes
* The number of users
* Bandwidth

---

<!-- Speaker notes: ~0:36. The reveal, with the concrete pattern.

The count example is the one that lands: reading 10,000 documents to
display "10,000 items" costs 10,000 reads every time the page loads. Store
the count instead. This is the shape of nearly every BaaS cost incident. -->

## Operations, not storage

* Reading 10,000 documents to display "10,000 items" costs **10,000 reads**
  — every page load

* Store the count. Update it on write

<div class="callout">

Nearly every BaaS billing surprise is a query that was fine with test data
and ruinous with real data.

</div>

---

<!-- Speaker notes: ~0:38. The choice. Be even-handed — BaaS is the right
answer for their project and not the right answer for everything.

The lock-in point is honest: your data model, your auth and your queries
become that vendor's shapes, and migrating later is real work. -->

## BaaS or your own backend?

| Reach for BaaS | Write your own |
|---|---|
| Small team, moving fast | Complex server-side logic |
| Standard auth and CRUD | Heavy reporting, real joins |
| Real-time is a feature you want | Strict cost predictability |
| Nobody wants to run servers | You need portability |

* Lock-in is real: your model, auth and queries become **their** shapes

---

<!-- Speaker notes: ~0:41. Common mistakes. The first is the one that
will actually happen to somebody in the room this semester. -->

## Common mistakes

* Shipping **development security rules** — the single commonest failure

* Assuming the client config is a secret

- Modelling relationally, then discovering there are no joins
- Reading a whole collection to compute something you could store
- Letting an assistant scaffold the backend without reading the rules it wrote

---

<!-- Speaker notes: ~0:43. Summary and close. Return to the opening: they
now know exactly why the refresh lost everything, and what the five jobs
are.

Leave the callout up for questions. -->

## Summary

- Five jobs exist whoever does them: **persistence, identity,
  authorisation, server logic, operations**
- BaaS rents all five — for control, portability and predictable cost
- The client config is **public**. **Security rules are the backend**
- Model around your **queries**; duplication is a deliberate trade
- Cost is **per operation**, not per gigabyte

<div class="callout">

"It works" and "it is safe" are different tests, and only one of them
happens automatically.

</div>
