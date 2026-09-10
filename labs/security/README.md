# AIAP Security Lab

Generated code is not neutral code. This lab is about what an AI assistant
quietly leaves out, how attackers exploit that, and what you can put in
place so it stops being your problem.

## What you'll learn

- Get an assistant to produce a vulnerable implementation, then get it to
  find its own vulnerability
- Recognise the four failures that dominate AI-generated code: missing
  input validation, injection, hardcoded secrets, insecure defaults
- Verify that every dependency in a project **actually exists** before
  installing it, and explain why that check is now necessary
- Defend an AI feature against prompt injection from untrusted input
- Turn on the free automated scanning GitHub already gives you

## Table of Contents

1. [Why generated code fails differently](#1-why-generated-code-fails-differently)
2. [The missing-validation problem](#2-the-missing-validation-problem)
3. [Hallucinated dependencies](#3-hallucinated-dependencies)
4. [Secrets](#4-secrets)
5. [Prompt injection in your own app](#5-prompt-injection-in-your-own-app)
6. [Automating the boring half](#6-automating-the-boring-half)
7. [Common mistakes](#common-mistakes)
8. [Summary](#summary)

## Getting started

1. Open a Codespace on **your own copy** of the module repo.
2. Move into this lab and install its dependencies:

   ```bash
   cd labs/security
   pip install -r requirements.txt
   ```

3. Check the tools you need are present:

   ```bash
   python check_setup.py
   ```

---

## 1. Why generated code fails differently

An assistant trained on public code learned from the vulnerable examples
too. It produces code that *looks* like working code — plausible names,
sensible structure, confident comments — because looking right is what it
optimises for. It has no threat model unless you give it one.

The measurable consequence: in 2026 testing, **44% of AI code-generation
tasks introduced at least one known vulnerability when no security
instruction was given.**

Read that number again, because the interesting part is the condition.
*When no security instruction was given.* The vulnerability rate is partly
a function of what you asked for — which makes it something you control.

### DIY 1: Make it fail, then make it notice

1. Ask your AI assistant, with no security framing at all:
   *"Write a Python function that looks up a user in a SQLite database by
   username and returns their row."*
2. Save what it gives you as `lookup_naive.py`.
3. Read it. Does it build the SQL by string formatting or f-string? Does
   it validate anything?
4. Now ask the **same assistant** in a fresh conversation:
   *"Review this code as a security engineer. What could an attacker do?"*
   Paste the code.
5. Record both the code and the review in `findings.md`.

**What you should have**

`findings.md` containing the original function, the review, and one
sentence in your own words naming the vulnerability class. In most runs
step 1 produces string-interpolated SQL and step 4 correctly identifies it
as SQL injection.

<details><summary>Hint</summary>

If step 1 happens to produce parameterised SQL (`?` placeholders), you got
a good roll — say so in `findings.md`, then re-run the prompt two or three
more times and record how many of the attempts were safe. That variability
*is* the finding: the same prompt does not reliably give the same safety.

Ask step 4 in a **new conversation**. In the same thread the assistant has
already committed to that code being good, and tends to defend it.

</details>

---

## 2. The missing-validation problem

The single commonest defect in generated code is not exotic. It is input
that reaches storage, a query, or a page without anyone checking it.

Assistants omit validation because you did not ask for it and because the
happy path is what makes the example readable.

### DIY 2: Add the checks that were never asked for

`vulnerable_app.py` in this folder is a small note-taking API. It works.
It was generated. It is not safe.

1. Run it and confirm it works:

   ```bash
   python vulnerable_app.py
   ```

2. Find **three** places where user input reaches storage or output with
   no validation.
3. For each, write down what an attacker could send.
4. Fix all three. You may use an assistant — but you must be able to
   explain each fix.
5. Re-run and confirm the app still works.

**What you should have**

Three fixes, and in `findings.md` a short table: the input, what an
attacker could send, and what your fix does about it.

<details><summary>Hint</summary>

Look for anywhere a value taken from a request is used without being
examined first: written straight into a data structure, concatenated into
a query, or returned in a response body.

"Validate" means decide what you *will* accept and reject everything else
— a length limit, a type, an allowed character set. A blocklist of bad
inputs is not validation; there is always another bad input.

</details>

---

## 3. Hallucinated dependencies

This is the newest attack in the lab and the one with no pre-AI equivalent.

An assistant suggests `import fastjsonparser`. The package does not exist —
the model invented a plausible name. Historically that was a harmless
error: `pip install` fails, you move on.

It stopped being harmless when attackers noticed two things:

- Roughly **19.7%** of AI-suggested dependencies point at packages that
  were never published.
- Hallucinations are **repeatable**. Re-running the same prompt ten times,
  **43%** of hallucinated names came back every single time.

Repeatable means predictable. An attacker runs the prompts a student would
run, collects the invented names, and registers them. The name is real
now, and it contains whatever they put in it. This is **slopsquatting**.

It is not theoretical: in January 2026 a hallucinated npm package called
`react-codeshift` reached **237 GitHub repositories** through AI-generated
agent skill files, and download attempts from autonomous agents were
recorded as soon as it was registered.

### DIY 3: Verify before you install

1. Ask an assistant: *"Give me a requirements.txt for a Python project
   that parses PDFs, does sentiment analysis, and caches results in
   Redis."*
2. Save it as `suspect-requirements.txt`.
3. **Do not install it.**
4. Complete `verify_deps.py` so that it reads a requirements file and, for
   each package, checks whether it exists on PyPI — reporting each as
   `OK` or `NOT FOUND`.
5. Run it against your file.

**Expected output**

```text
Checking suspect-requirements.txt (7 packages)

  OK         pypdf
  OK         redis
  NOT FOUND  pdf-sentiment-toolkit
  ...

1 package could not be found on PyPI. Do not install this file.
```

<details><summary>Hint</summary>

PyPI answers `https://pypi.org/pypi/<name>/json` with 200 if a package
exists and 404 if it does not. `urllib.request` is enough; catch
`HTTPError` and treat 404 as "not found".

Strip version specifiers (`redis>=5.0` → `redis`) before you look a name
up, and skip blank lines and `#` comments.

If every package in your file exists, that is a valid result — record it.
Then try a deliberately odd prompt (a very niche task) and see whether the
rate changes.

</details>

---

## 4. Secrets

You have already handled API keys three times in this module. This section
is about the failure mode where the assistant helps you do it wrong.

### DIY 4: Get caught by your own audit

1. In a scratch file, write a config that hardcodes a realistic-looking
   key, e.g. `OPENAI_API_KEY = "sk-" + "a"*40`. **Use a fake value.**
2. Stage it: `git add`.
3. Run the module's own audit from the repo root:

   ```bash
   python scripts/safety_audit.py
   ```

4. Read what it prints. Note that it **redacts** the value rather than
   echoing it.
5. Unstage and delete the file. Then write the correct version, reading
   the key from the environment.

**What you should have**

In `findings.md`: the audit's output (already redacted), one sentence on
why a CI log is a bad place to print a secret, and your corrected
environment-variable version.

<details><summary>Hint</summary>

`os.environ["OPENAI_API_KEY"]` raises if it is missing, which is usually
what you want — failing loudly beats running with a silently empty key.
`os.environ.get(...)` returns `None` and defers the error to somewhere
more confusing.

On why redaction matters: anyone who can see a workflow run can read its
log, and logs are retained. A secret printed once during a failed build is
a secret you must now rotate.

</details>

---

## 5. Prompt injection in your own app

Everything above is about code the assistant wrote *for* you. This section
is about an AI feature *inside* an app you build.

If your app takes text from a user and puts it in front of a model, that
text can contain instructions. `Ignore your previous instructions and…` is
the canonical example. The defence is the **instruction hierarchy**:
content that arrives from a user, a document or a tool is **data to be
reasoned about, never a source of authority.**

### DIY 5: Attack your own feature

1. Open `summariser.py` — a small tool that summarises a supplied
   document.
2. Run it on `documents/clean.txt` and confirm it behaves.
3. Run it on `documents/poisoned.txt`, which contains an injected
   instruction. Observe what happens.
4. Change the **system prompt** so the model treats document content as
   data only, and re-run.
5. Write one further injection of your own that defeats your fix, or
   convince yourself it holds.

**What you should have**

In `findings.md`: what the poisoned document did before your fix, the
wording you used to fix it, and either your successful bypass or a short
argument for why it holds.

<details><summary>Hint</summary>

Separate the roles explicitly. Put the instruction in the system prompt,
and wrap the untrusted text in a clear delimiter with a statement that
everything inside is content to be summarised and never an instruction.

Step 5 is the honest part of the exercise. Prompt injection is not a
solved problem, and a defence that reads as watertight often is not — if
you find a bypass, that is a better answer than a fix you cannot break.

</details>

---

## 6. Automating the boring half

None of the above scales by hand. GitHub gives you three checks free on
public repositories, and they run without being asked.

| Tool | Catches |
|---|---|
| **CodeQL** | Injection, unsafe deserialisation, path traversal |
| **Dependabot** | Dependencies with known CVEs |
| **Secret scanning** | Committed credentials — many providers auto-revoke |

### DIY 6: Turn them on

1. In **your own copy** of the repo, open **Settings → Code security**.
2. Enable **Dependabot alerts**, **secret scanning**, and **CodeQL**.
3. Add a workflow that runs CodeQL on every push, using the starter
   template GitHub offers.
4. Push, and watch it run in the **Actions** tab.
5. Read the first finding, if any, and decide honestly: real, or noise?

**What you should have**

A green (or informatively red) CodeQL run in your Actions tab, and in
`findings.md` one sentence on the first finding and your judgement of it.

<details><summary>Hint</summary>

Settings → Code security → *Set up* beside CodeQL analysis → **Default**
is enough; you do not need the advanced configuration.

If it reports nothing, that is a fine outcome — say so. To see it work,
temporarily reintroduce one of the DIY 2 vulnerabilities on a branch and
watch it get flagged. Do not merge that branch.

</details>

---

## Common mistakes

- **Asking "is this secure?"** The assistant will usually say yes. Ask
  *"what could an attacker do with this?"* — an open question it has to
  answer with specifics.
- **Reviewing in the same conversation that wrote the code.** It has
  already committed to that code being good and will defend it. Start a
  fresh one.
- **Treating a clean scan as proof.** CodeQL finds the classes it knows.
  Nothing scans for the logic flaw where your API returns other people's
  notes.
- **Blocklisting instead of validating.** Deciding what you accept is
  finite; enumerating what you reject is not.
- **Installing first and checking later.** With slopsquatting, installing
  *is* the compromise. Verification has to come first.

## Summary

- Generated code is not neutral: **44%** of tasks introduced a known
  vulnerability when nobody asked for security — and asking changes that
  number, which makes it your lever.
- The dominant defects are ordinary: missing validation, injection,
  hardcoded secrets, insecure defaults.
- **Slopsquatting** is the genuinely new one. Hallucinated package names
  are *repeatable*, which makes them registrable. Verify a dependency
  exists before you install it.
- Untrusted text is **data, never instructions** — that is the whole of
  prompt-injection defence, and it is not fully solved.
- Turn on CodeQL, Dependabot and secret scanning. They are free and they
  never get bored.

The through-line: you are accountable for code you did not write, and the
only thing that scales is making the machine check the machine.
