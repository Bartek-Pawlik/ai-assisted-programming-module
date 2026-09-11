# AI-Assisted Programming

Everything for the **AI-Assisted Programming** module (semester 1) at
Atlantic Technological University: the lectures, the labs, and an MCQ
practice app.

### Start here → **[danielcregg.is-a.dev/ai-assisted-programming](https://danielcregg.is-a.dev/ai-assisted-programming/)**

The whole module in one page — every lecture, every lab and the MCQ
practice, readable in the browser with nothing to install.

## Before the first lab

1. **A GitHub account under your real name.** You will be sending links
   to it all semester, and it is the account an employer will look at.
2. **The [GitHub Student Developer Pack](https://education.github.com/pack)**
   — free for verified students. It gives you the Copilot Student plan
   (the editor assistant and the terminal coding agent this module uses)
   and Pro-level Codespaces. Verification can take a few days, so apply
   early.
3. **Moodle enrolment.** The group password is given out in the first
   lecture, not published.

## Doing the labs

You work in **your own copy** of this repo:

1. Click **Use this template → Create a new repository** (green button,
   top-right). Name it anything; **make it Private** — it's your work.
   Don't *Fork*: a fork of a public repo can never be made private.
2. On *your* repo: **Code → Codespaces → Create codespace**. Python 3.12,
   Node 22 and the `gh` CLI are already there.
3. Open this week's lab folder under `labs/` and follow its README.

Details — including how to pull corrections into your copy mid-semester —
in **[labs/README.md](labs/README.md)**. Read-only lab pages are also on
the [site](https://danielcregg.is-a.dev/ai-assisted-programming/labs/),
always the current version.

One scheduled lab (RAG) needs a free API key of your own, and the CLI
agents lab needs you to sign in to a coding agent with your GitHub or
Google account. Each README says what, and how. Nothing in the module
costs money. **Never commit a key** — put it
in a `.env`, which is gitignored and rejected by the repo's safety audit.

## Assessment

| Component | Weight | When |
|---|---|---|
| MCQ 1 | 32% | Week 7, in person, during the lab slot |
| MCQ 2 | 32% | Week 12, in person, during the lab slot |
| Practical Assessments 1–9 | 4% each | One per lab, on Moodle, open for that lab's week |

The **Practical Assessments** are short Moodle questions, one for each
lab, open from the Monday to the Sunday of the lab's week — do each
whenever suits you that week. You may use AI tools for them, as you do in
the labs. They are built so that pasting the question into an assistant is
not enough on its own: each asks about the lab code in front of you, what
it actually does when you run it, or what is true right now. A missed one
counts as zero.

The **MCQs** are drawn from the lectures *and* the labs. Practise with the
[MCQ practice app](https://danielcregg.is-a.dev/ai-assisted-programming/practice/):
self-test quizzes on every topic, with your progress kept in your browser
only.

## Module schedule

<!-- current-week:start -->
> 🗓️ **Semester has not started yet** — teaching begins the week of 14 Sep 2026.
<!-- current-week:end -->

| Week | Topic | Lecture | Lab |
|---|---|---|---|
| 1 | Module Introduction | [slides](weeks/week-01-introduction/slides.md) | _no lab in week 1_ |
| 2 | AIAP Overview | [slides](weeks/week-02-overview/slides.md) | [lab](labs/setup/) |
| 3 | Prompting & Context Engineering | [slides](weeks/week-03-prompting/slides.md) | [lab](labs/prompting/) |
| 4 | Retrieval & Grounding | [slides](weeks/week-04-rag/slides.md) | [lab](labs/rag/) |
| 5 | MCP | [slides](weeks/week-05-mcp/slides.md) | [lab](labs/mcp/) |
| 6 | Coding Agents | [slides](weeks/week-06-agents/slides.md) | [lab](labs/agents/) |
| — | Reading week | [details](weeks/week-06b-reading-week/README.md) | — |
| 7 | **MCQ 1** (32%) | [details](weeks/week-07-mcq1/README.md) | — |
| 8 | Security of AI-Generated Code | [slides](weeks/week-08-security/slides.md) | [lab](labs/security/) |
| 9 | CLI Coding Agents | [slides](weeks/week-09-cli-agents/slides.md) | [lab](labs/cli-agents/) |
| 10 | CI/CD & Evals | [slides](weeks/week-10-cicd/slides.md) | [lab](labs/cicd/) |
| 11 | Vibe Coding & Spec-Driven | [slides](weeks/week-11-vibe-coding/slides.md) | [lab](labs/vibe-coding/) |
| 12 | **MCQ 2** (32%) | [details](weeks/week-12-mcq2/README.md) | — |

Reading week is always the week of the Irish October bank holiday, with
six teaching weeks either side.

### The everyday uses, and where you practise them

Four things you will do with an assistant most days are not weeks of their
own. They recur through the labs, so you meet each one more than once:

| You want to… | Practised in |
|---|---|
| **Explain** code you did not write | [setup DIY 4](labs/setup/README.md#diy-4-give-it-something-it-cannot-guess), [agents DIY 1](labs/agents/README.md#diy-1-understand-code-you-did-not-write) |
| **Debug** from an error or a failing test | [prompting DIY 6](labs/prompting/README.md#diy-6-chain-of-thought-on-a-real-bug), [cli-agents DIY 8](labs/cli-agents/README.md#diy-8-a-script-that-explains-a-failure) |
| **Write tests**, before or after the code | [prompting DIY 8](labs/prompting/README.md#diy-8-tests-first), [cicd DIY 1](labs/cicd/README.md#diy-1-make-it-run-your-tests), [cicd DIY 5](labs/cicd/README.md#diy-5-climb-the-assertion-ladder) |
| **Review** a change you did not watch being made | [agents DIY 2](labs/agents/README.md#diy-2-refactor-with-the-diff-open), [cicd DIY 3](labs/cicd/README.md#diy-3-a-review-step-that-cannot-lie), [vibe-coding DIY 2](labs/vibe-coding/README.md#diy-2-find-something-you-would-not-ship) |

## Module info

- [Module overview — weekly topics and what each week covers](module/module-overview.md)

<details>
<summary>How the repo is put together (for maintainers)</summary>

- **Lectures** are Marp markdown, one deck per teaching week in
  `weeks/week-NN-<topic>/slides.md`. All ten are written. Every deck is
  self-contained and names no lecturer or institution, so any week can be
  lifted into another course unchanged; the introduction may state its
  own schedule and link its own site. `scripts/check_deck_portability.py`
  enforces that.
- **Labs** are plain Python under `labs/<topic>/`, addressed by topic
  rather than week number so that a reshuffled schedule never breaks a
  student's instructions.
- **Three GitHub Actions workflows.** `marp` runs on every push to `main`:
  it runs the nine gates (safety audit, links, snippets, lab code, practice
  bank, lab and deck structure, speaker notes, site index), renders every
  deck to HTML and PDF, builds the lab pages and the practice app, and
  publishes the site straight to GitHub Pages — nothing is committed back.
  `current-week` runs every Monday and rewrites the banner above this
  schedule. Both are guarded to run only in this repository, never in a
  student's copy. `course-sync` is the inverse: it runs only in a
  student's copy, nightly, and commits any changed lectures, lab
  instructions and READMEs from this repo into theirs (never their code,
  never a course file they edited). It needs this repository to be public.
- **Conventions and editing rules** live in [`AGENTS.md`](AGENTS.md)
  (`CLAUDE.md` imports it). Local preview: `npm install`, then
  `npm run preview`.

</details>

## For AI tools

Read [`AGENTS.md`](AGENTS.md) first — it defines the conventions this repo
guarantees, and how to behave depending on whose copy you are in. (`CLAUDE.md`
imports it, so Claude Code reads the same file.)
