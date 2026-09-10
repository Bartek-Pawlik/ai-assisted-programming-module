# AI-Assisted Programming

Everything for the **AI-Assisted Programming** module (semester 1) at
Atlantic Technological University: the lectures, the labs, and an MCQ
practice app.

### Start here → **[danielcregg.is-a.dev/ai-assisted-programming](https://danielcregg.is-a.dev/ai-assisted-programming/)**

That's the whole module in one page — every lecture, every lab and the
MCQ practice, all readable in the browser with nothing to install.

**Doing the labs?** You need your own copy: click **Use this template →
Create a new repository** (green button, top-right). Name it whatever you
like and **you may set it to Private** — it's your work. Then on *your*
repo choose **Code → Codespaces → Create codespace**: Python, Node and the
`gh` CLI are already set up, nothing to install. Pick a lab folder under
`labs/` and follow its README. Details in **[labs/README.md](labs/README.md)**.

**How it's assessed:** two in-person MCQs (32% each) and nine short
**Practical Assessments** on Moodle (4% each), one for each lab. Each is
open for its lab's week — do it whenever suits you that week.

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
| 7 | **MCQ 1** (32%) | [details](weeks/week-07-mcq1/README.md) | — |
| 8 | Security of AI-Generated Code | [slides](weeks/week-08-security/slides.md) | [lab](labs/security/) |
| 9 | CLI Coding Agents | [slides](weeks/week-09-cli-agents/slides.md) | [lab](labs/cli-agents/) |
| 10 | CI/CD & Evals | [slides](weeks/week-10-cicd/slides.md) | [lab](labs/cicd/) |
| 11 | Vibe Coding & Spec-Driven | [slides](weeks/week-11-vibe-coding/slides.md) | [lab](labs/vibe-coding/) |
| 12 | **MCQ 2** (32%) | [details](weeks/week-12-mcq2/README.md) | — |

**Scheduling rule:** reading week always falls on the week of the Irish
October bank holiday, with 6 teaching weeks before it and 6 after.

**Assessment:** MCQ 1 (32%) and MCQ 2 (32%), held in person during lab
slots, and nine Practical Assessments (4% each) on Moodle — one for each
lab, open for that lab's week.

## Labs

All labs live in this repository — **[labs/](labs/README.md)** — one
folder per lab with the instructions (README) and its starter code.
Students: **Use this template** to make your own copy, open a Codespace on
it, pick a lab folder, and follow its README. Read-only lab pages are also
published on the
[live site](https://danielcregg.is-a.dev/ai-assisted-programming/labs/),
which always shows the current instructions — so if a lab is corrected
mid-semester, read it there. GitHub Classroom is retired.

Two labs need a free API key of your own (RAG, MCP), and the CLI agents
lab needs you to sign in to a coding agent with your GitHub or Google
account. Each README says what, and how. **Never commit a key** — put it
in a `.env`, which is gitignored.

A tenth folder, **[labs/baas](labs/baas/)**, is optional extra material:
a React frontend and a FastAPI backend on a hosted database. It is not in
the schedule and not assessed.

## Practical Assessments

Nine, one for each lab, each worth 4% and each open for its lab's week on
Moodle. You may use AI tools for them, as you do in the labs. They are
built so that pasting a question into an assistant is not enough on its
own: each one asks about the lab code in front of you, what it actually
does when you run it, or what is true right now.

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
