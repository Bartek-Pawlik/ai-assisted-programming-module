# AI-Assisted Programming

Everything for the **AI-Assisted Programming** module (semester 1) at
Atlantic Technological University: the lectures, the labs, the project
brief, and an MCQ practice app.

### Start here → **[danielcregg.is-a.dev/ai-assisted-programming](https://danielcregg.is-a.dev/ai-assisted-programming/)**

That's the whole module in one page — every lecture, every lab, the
project brief and the MCQ practice, all readable in the browser with
nothing to install.

**Doing the labs?** You need your own copy: click **Use this template →
Create a new repository** (green button, top-right). Name it whatever you
like and **you may set it to Private** — it's your work. Then on *your*
repo choose **Code → Codespaces → Create codespace**: Python, Node and the
`gh` CLI are already set up, nothing to install. Pick a lab folder under
`labs/` and follow its README. Details in **[labs/README.md](labs/README.md)**.

**Doing the project?** It's 60% of the module. The brief is
**[project/brief.md](project/brief.md)** — read it in week 2, not week 10.

**Practising for the MCQs?** Use the
[practice app](https://danielcregg.is-a.dev/ai-assisted-programming/practice/)
on the live site.

<details>
<summary>How the repo is put together (for maintainers)</summary>

Lectures are **Marp markdown** (`weeks/*/slides.md`) — edit the markdown,
push, and CI re-renders the HTML slides and a PDF, then publishes the site
straight from the workflow. Labs are plain Python (plus one TypeScript
frontend) under `labs/<topic>/`, each with its instructions in a README.
Conventions and editing rules live in [`CLAUDE.md`](CLAUDE.md).

All ten teaching decks are written. Every deck except the module
introduction is self-contained and carries no lecturer or institution
name, so any week can be lifted into another course unchanged —
`scripts/check_deck_portability.py` enforces that.

</details>

## Module schedule

<!-- current-week:start -->
> 🗓️ **Semester has not started yet** — teaching begins the week of 14 Sep 2026.
<!-- current-week:end -->

| Week | Topic | Lecture | Lab |
|---|---|---|---|
| 1 | Module Introduction | [slides](weeks/week-01-introduction/slides.md) | _no lab in week 1_ |
| 2 | AIAP Overview | [slides](weeks/week-02-overview/slides.md) | [lab](labs/setup/) |
| 3 | Prompting & Context Engineering | [slides](weeks/week-03-prompting/slides.md) | [lab](labs/prompting/) |
| 4 | RAG & Retrieval Strategy | [slides](weeks/week-04-rag/slides.md) | [lab](labs/rag/) |
| 5 | MCP | [slides](weeks/week-05-mcp/slides.md) | [lab](labs/mcp/) |
| 6 | Coding Agents | [slides](weeks/week-06-agents/slides.md) | [lab](labs/agents/) |
| — | Reading week | [details](weeks/week-06b-reading-week/README.md) | — |
| 7 | **MCQ 1** (20%) | [details](weeks/week-07-mcq1/README.md) | — |
| 8 | Security of AI-Generated Code | [slides](weeks/week-08-security/slides.md) | [lab](labs/security/) |
| 9 | BaaS | [slides](weeks/week-09-baas/slides.md) | [lab](labs/baas/) |
| 10 | CI/CD & Evals | [slides](weeks/week-10-cicd/slides.md) | [lab](labs/cicd/) |
| 11 | Vibe Coding & Spec-Driven | [slides](weeks/week-11-vibe-coding/slides.md) | [lab](labs/vibe-coding/) |
| 12 | **MCQ 2** (20%) | [details](weeks/week-12-mcq2/README.md) | — |

**Scheduling rule:** reading week always falls on the week of the Irish
October bank holiday, with 6 teaching weeks before it and 6 after.

**Assessment:** MCQ 1 (20%), MCQ 2 (20%), and the
[project](project/brief.md) (60%). The MCQs are held in person during lab
slots.

## Labs

All labs live in this repository — **[labs/](labs/README.md)** — one
folder per lab with the instructions (README) and its starter code.
Students: **Use this template** to make your own copy, open a Codespace on
it, pick a lab folder, and follow its README. Read-only lab pages are also
published on the
[live site](https://danielcregg.is-a.dev/ai-assisted-programming/labs/),
which always shows the current instructions — so if a lab is corrected
mid-semester, read it there. GitHub Classroom is retired.

Three labs need a free API key of your own (RAG, MCP, BaaS). Each says
which, and how to get one, in its README. **Never commit a key** — put it
in a `.env`, which is gitignored.

## The project

60% of the module, due at the end of week 12.
**[Read the brief](project/brief.md).** You build an application in a
language of your choice that incorporates some AI technology, using AI
tools to help you — and you present and defend it.

## MCQ practice

Self-test quizzes generated from the module's own content:
**[MCQ practice](https://danielcregg.is-a.dev/ai-assisted-programming/practice/)**.
Per-topic progress is stored in your browser only. The practice bank
(`practice/bank/`) is authored for this purpose and is separate from any
assessment material.

## Module info

- [Module overview — weekly topics and what each week covers](module/module-overview.md)

## For AI tools

Read [`CLAUDE.md`](CLAUDE.md) first — it defines the conventions this repo
guarantees, and how to behave depending on whose copy you are in.
