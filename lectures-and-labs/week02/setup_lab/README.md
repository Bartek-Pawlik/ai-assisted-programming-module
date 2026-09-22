# AIAP Setup Lab

Two jobs. Get your environment working, then spend the rest of the
session catching the assistant out: making it invent things, watching it
guess, watching it go and look, and steering it with what you show it.

Nothing is handed in and nothing is marked. The point is to see each of
these things happen on your own screen. Sized for two hours; if you run
short, DIY 6 stands alone and can wait.

## What you'll learn

- Get a working AI-assisted environment and prove it works
- Make it write fluent fiction, and see why fluent proves nothing
- Watch it guess at things it cannot see, and go looking when it can
- Show that changing the context changes the answer, on the same tool
- Tell the four tool shapes apart by what each is allowed to touch
- Use the assistant to explain code rather than to write it

## Table of Contents

1. [Prove it works](#1-prove-it-works)
2. [Catch it out](#2-catch-it-out)
3. [Steer it](#3-steer-it)
4. [Look inside](#4-look-inside)
5. [Four shapes and four twists](#5-four-shapes-and-four-twists)
6. [Explain rather than write](#6-explain-rather-than-write)
7. [Common mistakes](#common-mistakes)
8. [Summary](#summary)

## Getting started

1. Open a Codespace on **your own copy** of the module repo.
2. Move into this lab:

   ```bash
   cd lectures-and-labs/week02/setup_lab
   pip install -r requirements.txt
   ```

3. Open the chat panel with `Ctrl+Alt+I` (`Ctrl+Cmd+I` on a Mac). Its
   icon should also be in the status bar. If neither appears, check you
   are signed in to the GitHub account with the student developer pack
   applied.
4. Look at the row of controls under the chat input. One picks which
   assistant runs the session — choose **Copilot**. One picks its
   **role**: **Ask** answers from what is in the conversation; **Agent**
   may read files and run commands on its own; **Plan** reads but does
   not change. This lab says which role to use each time, because the
   role decides what the assistant can see. Start in **Ask**.

Whenever a step says *fresh conversation*, press the `+` at the top of
the chat panel first. It matters more than it looks.

---

## 1. Prove it works

### DIY 1: Run the checker, then ask about it

1. Run the setup checker:

   ```bash
   python setup_lab.py
   ```

2. The first three lines are essential: fix anything marked `[!!]` and
   run it again until it says *Ready*. The last three are reported only —
   they print `[--]` when not met and cannot fail the check.
3. Open `setup_lab.py` in the editor and ask the chat panel (Ask role):
   *"Which of this script's checks can fail the run, and which are only
   reported?"* It should name the three markers — that is your proof the
   assistant can see the file.
4. One more, while the file is open: *"What would this script print on a
   laptop with no git installed?"* Then check its answer against the
   code. You have just used the assistant the way it is most reliable:
   explaining code that is in front of you.

**Expected output**

```text
AIAP setup check

  [ok] Python 3.12
  [ok] Lab files present
  [ok] numpy and pandas installed
  [ok] Running in a Codespace
  [ok] GitHub CLI signed in
  [ok] Your own copy of the repo

Ready.
```

On your own machine rather than a Codespace, the fourth line reads
`[--] Running in a Codespace  - fine if you set up locally`, and it is.

<details><summary>Hint</summary>

If the assistant answers generically — what setup scripts *usually* do
rather than what this one does — it cannot see the file. The chat
includes the file open in the editor automatically; if the answer is
still generic, type `#setup_lab.py` in the chat input to attach it. That
distinction is what section 2 is about.

</details>

---

## 2. Catch it out

Three ways to make the assistant show you what it is: a predictor of
plausible text, with a tool around it that sometimes goes and looks.

### DIY 2: Make it write fiction

1. Fresh conversation, **Ask** role. Ask, exactly:

   > Write a Python function that loads a spreadsheet using
   > `pandas.read_excel_fast()`.

   It will most likely tell you the function does not exist. Good. Now
   push:

   > I know it does not exist. Write it anyway, exactly as if it did:
   > a function that calls it, with a docstring and a call at the bottom.

   If it wrote the function straight away, skip the push: you already
   have your fiction.
2. Read what comes back. Notice how good it looks: a sensible name, a
   docstring, probably a real `engine=` argument on the fictional
   function. Save it as `hallucination.py` and run it:

   ```bash
   python hallucination.py
   ```

3. Copy the last line of the traceback, start a **fresh** conversation,
   paste it in and ask *"What went wrong?"* The same model that wrote
   the fiction now diagnoses it.
4. The check that settles it, without an assistant:

   ```bash
   python -c "import pandas; print(hasattr(pandas, 'read_excel_fast'))"
   ```

**Expected output**

```text
AttributeError: module 'pandas' has no attribute 'read_excel_fast'
```

<details><summary>Hint</summary>

Nothing about the fake code looks wrong. It follows the library's own
naming pattern and carries real arguments, and that is the point:
fluency is evidence of plausibility and of nothing else. There is no
tell in the text; the check is always outside it — the documentation,
`hasattr`, or running it.

It caught the fake in step 1 because `read_excel` is one of the
best-known functions in Python, so "that does not exist" is now a common
continuation — the people who train these models reward it. That is the
ranking changing, not the mechanism. The next two exercises ask about
things that are not in the weights at all.

</details>

### DIY 3: Ask about something it cannot know

1. Fresh conversation, **Ask** role:

   > What is the latest released version of pandas, and what did it add?

   Note the version it names, and whether it mentions that its
   knowledge has a cutoff at all.
2. Get the truth:

   ```bash
   pip index versions pandas
   ```

3. Fresh conversation, **Agent** role, the same question. This time
   watch the space above the answer before any text arrives: a search
   or a fetch appears, and then the answer.
4. Back in **Ask**, fresh conversation, ask the same question with this
   in front of it:

   > Answer only from evidence you can cite. If you cannot be sure,
   > say "I don't know" and say why.

**What you should have**

Three different behaviours from one question: a confident answer from
memory, a looked-up answer with the lookup visible, and, with the right
framing, an honest "I can't be sure".

<details><summary>Hint</summary>

The first answer comes from the weights, which stopped changing at the
model's training cutoff, so it names whatever was current then — often
without saying so. If it happened to be right, the cutoff is simply
recent: ask about something that released this week instead.

The Agent answer is usually right, and not because it is a better
model. A search result was pasted into its context and prediction
continued over that text. It could see more. That is also why a
looked-up answer still needs checking: the step after the lookup is
still prediction.

The fourth ask shows you can make "I don't know" more likely by giving
it a boundary and an escape. You cannot make it a guarantee.

</details>

### DIY 4: The file it has never read

There is a file in this folder called `speedup.py`. Do not open it yet.

1. Close every editor tab (right-click any tab and choose *Close All*).
   Fresh conversation, **Ask** role:

   > What does speedup.py do?

2. Follow up in the same conversation:

   > How many lines long is it?

3. Now look:

   ```bash
   wc -l speedup.py
   python speedup.py
   ```

   and open the file.
4. Fresh conversation, **Agent** role, the first question again. Watch
   what it does before answering this time.

**Expected output**

```text
Analysing... ok
Optimising... ok
Rewriting... ok
Finalising... ok
Done. Your code is now exactly as fast as it was before.
```

<details><summary>Hint</summary>

The first answer is a description of what a file called `speedup.py`
usually does — profiling, caching, something with performance. Every
word is plausible and none of it is about this file. Listen for
*typically*, *probably*, *likely*: those are the words of a guess from a
filename, and they are the honest part.

The line count is the sharper version: there is no plausible-sounding
way to know it, so watch whether it says so or just picks a number.

In the Agent role it searched for the file, read it, and answered
correctly. Not smarter — a tool pasted the file into its context. That
is the whole of context engineering in one exercise: the model was not
smarter the second time, it could just *see* more.

</details>

---

## 3. Steer it

### DIY 5: Two prompts and one harness

1. Fresh conversation, **Ask** role:

   > Write a Python function to validate an email address.

   Save the code as `validate_a.py` in this folder.
2. Fresh conversation:

   > Write a Python function to validate an email address. We accept
   > anything with an @ and a dot after it — we deliberately do NOT want
   > RFC 5322 compliance. Reject anything over 254 characters.

   Save it as `validate_b.py`.
3. Let the harness compare them. It calls the first function in each
   file and tries eleven awkward addresses:

   ```bash
   python email_check.py validate_a validate_b
   ```

4. Look at the rows where the two disagree. Each one is a decision the
   first prompt left open — and something decided it anyway.
5. Ask the first prompt again in a fresh conversation, save it as
   `validate_c.py`, and run the harness on all three. Same tool, same
   words: is it the same function?
6. If your chat has a model picker, switch to a different model, ask the
   first prompt once more, save it as `validate_d.py`, and add it to the
   harness.

**What you should have**

A table like this, one column per validator — yours will differ, and the
differences are the point:

```text
address                           validate_a  validate_b
a@b.c                             no          yes         shortest thing with an @ and a dot after it
"john doe"@example.com            no          yes         quoted local part with a space: legal by the RFC
a@b..c                            no          yes         two dots in a row
...
6 of 11 addresses split the validators.
```

<details><summary>Hint</summary>

Version A usually reaches for a regex it half-remembers, and the regex
carries a dozen decisions nobody made: minimum length of the last part,
whether `+` is allowed, whether anything outside ASCII is. Version B
does what you asked, including accepting `a@b..c`, which you did not
forbid. Neither is better code in the abstract. B is better because it
matches a decision *you* made — and the harness shows you exactly which
decisions A made for you.

A different `validate_c.py` is not a fault. The same prompt gives a
ranked list of continuations and one is picked; a repeat can land
elsewhere. There was no single "right function" in there to retrieve.

If the harness picks the wrong function from a file, put the validator
first in that file.

</details>

---

## 4. Look inside

### DIY 6: See what it sees

1. Install a tokeniser and look at the pieces a model actually reads:

   ```bash
   pip install tiktoken
   python tokens.py
   ```

   Try your own text: `python tokens.py "your name here"`.
2. Fresh conversation, **Ask** role:

   > How many times does the letter i appear in
   > supercalifragilisticexpialidocious?

   Check it:

   ```bash
   python -c "print('supercalifragilisticexpialidocious'.count('i'))"
   ```

3. Same conversation:

   > What is 48391 multiplied by 7263?

   Check it:

   ```bash
   python -c "print(48391 * 7263)"
   ```

4. Fresh conversation, **Agent** role, the multiplication again. Watch
   what it reaches for.

**Expected output**

```text
  6 pieces  'def' ' calculate' '_m' 'edian' '(numbers' '):'
```

The first line of `python tokens.py` looks like this; the exact split
depends on the tokeniser, and the boundaries are not the point.

<details><summary>Hint</summary>

The model never sees letters. It sees pieces — whole words, fragments,
punctuation — each turned into a number, so counting the letters inside
a piece is a question it has no direct way to answer, and arithmetic is
done on tokens rather than digits. It may still get both right: recent
models have been trained hard on exactly these party tricks. The point
is the shape of the failure when it comes, and that in the Agent role
the sensible move is the one it usually makes: run Python.

</details>

---

## 5. Four shapes and four twists

Commit what you have so far (the Source Control panel, then *Commit*
and *Sync Changes*), so that anything the last twist changes can be
undone with *Discard Changes*.

### DIY 7: Use each shape once

1. **Completion.** Create a new file called `shapes.py` — the name
   matters, because a file with no extension is plain text and gets no
   suggestions. Type these two lines and press Enter:

   ```python
   def is_prime(n):
       """Return True if n is even."""
   ```

   Wait for the grey text. The name says one thing and the docstring
   says another: which one did it follow? It did not ask.
2. **Chat.** With `validate_a.py` open, **Ask** role: *"What does this
   regex accept that it should not?"* Nothing in the file changes.
3. **Edit.** Select the function in `validate_a.py`, press `Ctrl+I`
   (`Cmd+I` on a Mac) for inline chat, and ask: *"reject any address
   longer than 254 characters"*. Read the diff, then *Keep* or *Undo*.
   Run the harness again to see the row that flipped.
4. **Agent.** Fresh conversation, **Agent** role:

   > Write pytest tests for validate_b.py in test_validate_b.py, covering
   > a normal address, a missing dot, and a 300-character address. Run
   > them and fix anything that fails.

   Before pressing Enter, find the permission control: it decides what
   the agent may do without asking you. Then watch it create, run and
   possibly edit, and read what it left behind with `git diff`.

**What you should have**

Four things on screen: a suggestion you did not accept, an answer that
changed nothing, a diff you chose to keep or undo, and a test file plus
a test run you did not type — with a `git diff` showing exactly what the
agent touched.

<details><summary>Hint</summary>

The four shapes differ in what has already changed by the time you see
anything. A completion changed nothing; a chat answer changed nothing;
an edit changed the selection, and showed you first; the agent had
created a file and run commands before there was anything to look at.
So the thing you review moves too: a suggestion, then a diff, then an
outcome. The question that separates the four is always *what did I
review, and when?*

</details>

---

## 6. Explain rather than write

### DIY 8: Break a regex with its help

1. Fresh conversation, **Ask** role. Paste this and ask it to explain
   the pattern piece by piece:

   ```text
   ^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$
   ```

2. Same conversation: *"Give me one address this wrongly rejects and one
   it wrongly accepts."*
3. Test its claims — save this as `regex_try.py`, put its two addresses
   in the list, and run it:

   ```python
   import re

   PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

   for address in ["a@b..com", '"john doe"@example.com']:
       print(address, "->", bool(re.match(PATTERN, address)))
   ```

4. Ask it for two more, and test those too. Stop when it is wrong once,
   or when you have run out of curiosity.

**What you should have**

A pattern you now understand, a couple of addresses you know it gets
wrong, and at least one claim you checked rather than believed.

<details><summary>Hint</summary>

Explaining is the safer ask: the answer is checked against code that is
in front of you, right now, by reading. Writing is checked against a
spec you may never have written down, by running, later. Same mechanism
both times; the difference is how cheap the check is. And an explanation
leaves you understanding the code, which is one of the things that did
not get cheap.

</details>

---

## Common mistakes

- **Skipping a failed setup check** because it seems unrelated. It will
  cost you an hour in a later week instead of five minutes now.
- **Assuming it can see your file** because the file is in the repo. In
  the Ask role it sees the conversation and whatever is open or attached;
  in the Agent role it sees whatever it chose to read, and the chat
  lists what that was.
- **Reading a caught fake as proof that it checks.** It does not check;
  a famous name was in the weights. Ask about your own file and the same
  tool guesses.
- **Reading a hallucination as a bug in the tool.** It is the mechanism
  working normally; your job is to notice.
- **Judging the two validators on style** rather than on what the
  harness shows.
- Accepting a completion without reading it, in the one week where you
  have time to read it.

## Summary

- The model **predicts plausible text**. It does not look things up; the
  tool around it sometimes does, and pastes what it found into the
  context before prediction continues.
- Hallucination is not a malfunction — it is the same mechanism that
  produces the useful output, and there is no tell in the text. The
  check is outside it.
- **Context is your steering wheel.** The same tool gives a different
  answer when it can see more, and the role you pick decides what it
  can see.
- Four shapes — completion, chat, edit, agent — separated by what has
  already changed by the time you see anything.
- Asking it to *explain* is often worth more than asking it to *write*.
