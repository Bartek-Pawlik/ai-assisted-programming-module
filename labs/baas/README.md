# AIAP Backend as a Service Lab

A React frontend and a FastAPI backend, talking to a hosted database. The
frontend is the part an assistant can build in ten minutes. This lab is
about the other four-fifths.

## What you'll learn

- Connect a real application to a hosted database and make data persist
- Explain why the client configuration is public, and what actually
  protects the data
- Write security rules and prove they block what they should
- Model data for a store with no joins
- Spot the query that is cheap on test data and ruinous on real data

## Table of Contents

1. [Get it running](#1-get-it-running)
2. [Connect the database](#2-connect-the-database)
3. [The config is public](#3-the-config-is-public)
4. [Modelling without joins](#4-modelling-without-joins)
5. [The cost model](#5-the-cost-model)
6. [Common mistakes](#common-mistakes)
7. [Summary](#summary)

## Getting started

1. Open a Codespace on **your own copy** of the module repo.
2. Install both halves:

   ```bash
   cd labs/baas
   pip install -r backend/requirements.txt
   cd frontend && npm install && cd ..
   ```

3. Run the backend and the frontend in two terminals:

   ```bash
   uvicorn backend.app.main:app --reload     # terminal 1
   cd frontend && npm run dev                # terminal 2
   ```

This lab needs a **free hosted-database project** of your own. Section 2
walks through creating one. Credentials go in `.env` files —
`frontend/.env.example` shows the shape. **Never commit a real one.**

---

## 1. Get it running

Before wiring anything up, confirm both halves work on their own.

### DIY 1: Run it with no database

1. Start the backend and open `http://localhost:8000/docs`.
2. Create a note through the interactive docs.
3. Run the backend tests:

   ```bash
   python -m pytest backend/tests
   ```

4. Open the frontend and add a note through the interface.
5. **Refresh the page.** Record what happens.

**Expected output**

```text
backend/tests/test_routes.py ....                                [100%]
4 passed

Frontend: note appears in the list.
After refresh: the list is empty.
```

<details><summary>Hint</summary>

Everything is in memory until you connect a database, so a refresh wipes
it. That is the gap between "looks like an app" and "is an app" — and it
is precisely the part an assistant will not build unless asked.

If the frontend cannot reach the backend, check the API base URL in
`frontend/src/api.ts` against the port uvicorn actually bound.

</details>

---

## 2. Connect the database

### DIY 2: Make data survive

1. Create a free project in a hosted document database and create a
   database within it.
2. Generate a service account credential for the backend.
3. Put its path in an environment variable — **not** in the code, and not
   in a committed file.
4. Complete the functions in `backend/app/firestore.py` so notes are read
   and written from the database.
5. Add a note, refresh, and confirm it survives.

**Expected output**

```text
$ curl localhost:8000/notes
[{"id":"a1b2c3","title":"Shopping","body":"milk, bread","owner":"..."}]

Frontend: note still present after refresh.
```

<details><summary>Hint</summary>

Read the credential path with `os.environ["..."]`, which raises if it is
missing. `os.environ.get(...)` returns `None` and defers the failure to
somewhere far more confusing.

Add the credential filename to `.gitignore` **before** you download it,
not after. The safety audit will reject it if it reaches the index, but
the cheapest place to stop it is before it exists.

</details>

---

## 3. The config is public

This is the section that matters most, and the one people are most
surprised by.

### DIY 3: Read your own secrets

1. Run the frontend and open your browser's developer tools.
2. Find the database configuration in the loaded JavaScript.
3. Copy the project identifier and API key out of it.
4. Write down: **who else can do exactly what you just did?**

**What you should have**

The config values you extracted from your own running app, and a one-line
answer to step 4.

<details><summary>Hint</summary>

Anyone with the URL. The client config ships in the bundle and is not a
secret — it was never meant to be one.

Which raises the obvious question, and it is the next exercise: if the
credentials are public, what stops a stranger reading your entire
database?

</details>

### DIY 4: Break in, then lock the door

1. Set your database rules to the permissive development default:

   ```text
   allow read, write: if true;
   ```

2. Using **only** the config you extracted in DIY 3, write a short script
   that reads every note — without going through your backend at all.
3. Confirm it works. That is the vulnerability.
4. Now write rules that allow a user to read and write **only their own**
   notes.
5. Re-run your script and confirm it is refused.

**Expected output**

```text
With open rules:
  Fetched 3 notes belonging to other users.   <-- the vulnerability

After rules applied:
  PERMISSION_DENIED: Missing or insufficient permissions.
```

<details><summary>Hint</summary>

The rule needs two halves: the request must be authenticated, and the
document's owner must match the authenticated user. Check ownership on
`resource.data` for reads and on `request.resource.data` for writes —
they are different objects and using the wrong one is the classic mistake.

Step 3 is the part worth sitting with. You attacked your own database
using nothing but values that ship to every visitor.

</details>

### DIY 5: Check what an assistant scaffolds

1. In a fresh conversation, ask an assistant to set up a hosted database
   for a notes app with authentication.
2. Read the rules it produces **before** running anything.
3. Record whether they were open, restrictive, or absent.
4. If they were open, ask it *"what could an attacker do with these
   rules?"* and record the answer.

**What you should have**

The rules it generated, your verdict on them, and its own answer when
challenged.

<details><summary>Hint</summary>

Open rules are extremely common in generated setups, because they are what
make the tutorial work. The assistant is not being careless — it is
optimising for the example running, and nobody asked it for security.

Note that it usually identifies the problem correctly when asked
directly. It had the knowledge; nothing in the first prompt made it apply
it.

</details>

---

## 4. Modelling without joins

### DIY 6: Model for the screen, not the schema

1. Add a feature: each note belongs to a **category**, and the interface
   shows the category name beside every note.
2. Design it relationally first — notes referencing a categories
   collection — and write down how many reads one screen of 20 notes
   costs.
3. Now design it denormalised, with the category name stored on the note.
   Count the reads again.
4. Implement whichever you choose.
5. Write down the cost of your choice — specifically, what happens when a
   category is renamed.

**What you should have**

Both read counts, your chosen design, and an honest statement of what it
costs you.

<details><summary>Hint</summary>

Relational: 20 notes plus a lookup per distinct category. Denormalised: 1
query. Document stores have no joins, so the assembly you would get free
in SQL becomes round trips you pay for.

Denormalising is a trade, not sloppiness — but a renamed category now has
to be updated on every note carrying it, and nothing in the database will
tell you when the copies disagree. Write down where each copy lives.

</details>

---

## 5. The cost model

### DIY 7: Find the ruinous query

1. Add a counter to the interface showing the total number of notes.
2. Implement it the obvious way: fetch the collection and count it.
3. Work out what that costs, in operations, at 10 notes and at 10,000.
4. Re-implement it so the count is **stored** and updated on write.
5. Compare the two costs per page load.

**What you should have**

```text
| Approach        | Reads at 10 notes | Reads at 10,000 | Per page load |
|-----------------|-------------------|-----------------|---------------|
| Fetch and count |                   |                 |               |
| Stored counter  |                   |                 |               |
```

<details><summary>Hint</summary>

Reading 10,000 documents to display the number 10,000 costs 10,000 reads,
every single time the page loads. The stored counter costs one.

This shape — fine on test data, ruinous on real data — is behind nearly
every surprise bill story you will hear. Billing is per **operation**, not
per gigabyte, and test datasets never reveal it.

</details>

---

## Common mistakes

- **Shipping development security rules.** The single commonest failure,
  and it is one line.
- Assuming the client config is a secret. It ships to every visitor.
- Checking ownership on the wrong object — `resource` for writes,
  `request.resource` for reads.
- Modelling relationally, then discovering there are no joins.
- Reading a whole collection to compute something you could have stored.
- Letting an assistant scaffold the backend without reading the rules it
  wrote.

## Summary

- Five jobs exist whoever does them: **persistence, identity,
  authorisation, server logic, operations**.
- The client config is **public by design**. **Security rules are the
  backend.**
- You can attack your own database with values that ship to every
  visitor — try it, then close it.
- Model around the **queries your screens need**; denormalising is a
  deliberate trade with a maintenance cost.
- Cost is **per operation**. The query that is fine on test data is the
  one that bites.
