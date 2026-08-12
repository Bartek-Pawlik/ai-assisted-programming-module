# AI-Assisted Programming — module repository design

*Design agreed 12 August 2026. Ports the model established by
`danielcregg/object-oriented-computing`, adapted where AIAP's content
differs.*

---

## Purpose

Make every artefact of the AI-Assisted Programming module plain text in one
version-controlled public repository, so that a human, a build server and an
AI assistant can all read it, check it and improve it. The repository is
simultaneously the source, the website, the student workspace, the quality
gate and the AI's instruction set.

The Object-Oriented Computing repo already proves this pattern. This spec
records where AIAP follows it and — more usefully — where AIAP cannot.

## Starting position

| | Before |
|---|---|
| Lectures | 9 PowerPoint decks in OneDrive; 3 orphaned Reveal.js conversions in a stale private repo |
| Labs | 11 GitHub Classroom template repos scattered across `DanielCreggOrganization` |
| Project | `aiap-project-template` (private org repo) holding `project-brief.md` and `AI-USAGE.md` |
| Assessment | MCQ 1, MCQ 2, project — weighting being changed to 20/20/60 |
| Weeks | 13 numbered, no reading week |
| Automated checks | none |
| Site | `danielcregg.github.io/AIAP-lecture-slides`, stale since November 2025 |

`danielcregg/AIAP-lecture-slides` is not migrated. It is a Reveal.js build
with `_site/` and `dist/` committed into git, plus voice-cloning and
video-generation experiments. It is superseded, not ported. It stays private
and untouched as a historical record.

## Decisions

### 1. Deck conversion is week-by-week, not up front

The repository ships complete — structure, gates, site, workflows — with
week 1 converted as the proof deck. Remaining decks convert ahead of the week
they are taught.

The PowerPoints stay in OneDrive as the fallback until each deck is converted
and verified. A week folder with no `slides.md` fails the structure gate, so
the build cannot silently ship a half-created week; unconverted weeks are
listed explicitly in `build_index.py`'s `PENDING_DECKS` until their deck
lands.

This spreads the largest cost in the project across the semester and lets the
2025 content be refreshed as it is converted rather than faithfully
reproducing material the field has moved past.

### 2. Labs move into the repository; GitHub Classroom is retired

All nine labs become `labs/<topic>/` in this repository. Students take one
template copy for the whole module rather than a Classroom repo per lab.

**Labs are addressed by topic, not by week number.** The current names are
week-addressed (`aiap-w3-lab-prompting`, `aiap-w10-lab-ai-cicd`), and the
13→12 restructure happening in this same change is exactly the churn that
argues against it. Week numbers move between years; student instructions
should not. The week number appears only in the README schedule table, where
it is one line to edit.

| Week | Lab folder | Source repo |
|---|---|---|
| 2 | `labs/setup/` | `aiap-w2-lab-setup-aiap-labs-template` |
| 3 | `labs/prompting/` | `aiap-w3-lab-prompting-aiap-labs-template` |
| 4 | `labs/rag/` | `aiap-w4-lab-rag-template` |
| 5 | `labs/mcp/` | `aiap-w5-lab-mcp-aiap-labs-template` |
| 6 | `labs/agents/` | `aiap-w6-lab-agents-template` |
| 8 | `labs/cli-coding-agents/` | `aiap-w8-lab-cli-coding-agent-template` |
| 9 | `labs/baas/` | `aiap-w9-lab-baas-template` |
| 10 | `labs/cicd/` | `aiap-w10-lab-ai-cicd-template` |
| 11 | `labs/vibe-coding/` | `aiap-lab-vibe-coding-template` |

The source repos are left in place, untouched. Nothing is deleted from the
organisation as part of this change.

**Partial loss (better than expected):** `aiap-w3-lab-prompting` carried
autograding in two halves. The **local** half — `scripts/run_and_grade.py`
and `scripts/setup_check.py` — migrated intact and still works, so a student
can still self-check a task in one command. Only the Classroom-hosted half
(`.github/workflows/classroom.yml`, `.github/scripts/score.py` and the score
badge) is gone. The lab README now frames the score as a self-check that
reports nowhere, rather than a submission.

### 3. Solutions and instructor material leave the public repository

A private `danielcregg/ai-assisted-programming-labs-solutions` holds the nine
files that must not ship:

    aiap-w4-lab-rag-template/INSTRUCTOR_GUIDE.md
    aiap-w4-lab-rag-template/solutions/{part2,part3,part4}_*_solution.py
    aiap-w4-lab-rag-template/solutions/README.md
    aiap-w5-lab-mcp-aiap-labs-template/INSTRUCTOR_NOTES.md
    aiap-w5-lab-mcp-aiap-labs-template/solutions/solution_news_mcp_{client,server}.py
    aiap-w6-lab-agents-template/INSTRUCTOR_GUIDE.md

This matters more here than in OOC, because AIAP's tutor brief (decision 6)
places no restriction on the assistant. The repository boundary is therefore
the only thing separating a student from a worked solution, and it has to
hold on its own.

A pre-migration scan of all eleven source repositories for credential-shaped
strings, `.env` files, private keys and service-account JSON found nothing.
The only match was `aiap-w9-lab-baas-template/frontend/.env.example`, which is
safe by design and ships.

### What the gates actually found (added after implementation)

The scan above was clean, but the gates were not. Four classes of problem
surfaced only once the checks ran, and all four are now fixed:

1. **Worked answers inside the exercise files.** Six of the ten blank
   worksheets in `labs/prompting/lab/prompts/` (tasks 1, 3, 5, 6, 7, 10) had
   somebody's completed answers appended to the template. Students were being
   handed the solutions inside the files they were supposed to fill in. This
   was not in `solutions/` and no filename suggested it.
2. **A real student's name in the project brief** — the worked example of a
   submission textbox quoted a GitHub URL from a previous year's cohort,
   which carried that student's name in the repo slug, alongside a personal
   SharePoint video link. Both replaced with generic placeholders. (The name
   is deliberately not repeated here: quoting it to document the fix would
   put it straight back into the repo.)
3. **Moodle group enrolment passwords** in the week-01 PowerPoint. The
   converted deck states that they are given out verbally instead, because
   the deck is published to a public website.
4. **Corrupted markdown in the CLI-agents lab** — four closing fences had
   been written *over* the first three characters of the following line
   (`` ```on't pipe… ``, `` ```heck version ``, `` ```ilot  # Then try… ``),
   plus one orphan fence rendering eight lines of prose as a code block.

Point 1 is the one worth remembering: the repo-boundary decision above
protects `solutions/`, and `solutions/` was never where the real leak was.

### 4. The project brief becomes canonical here

`project/brief.md`, `project/rubric.md` and `project/ai-usage-template.md`
live in this repository and publish to the site. The org template repo shrinks
to a bare starter that links back, so students still get their own repository
to build the project in, but there is one source for the brief and it is
versioned alongside the module it belongs to.

### 5. Twelve weeks plus a derived reading week

Week 13 ("Project Review") is dropped — it was a placeholder. Week 12 ends the
module on MCQ 2.

Reading week is not stored, it is computed, using the same rule as OOC:
**reading week is the week of the last Monday in October; week 1 begins six
weeks before it; six teaching weeks sit each side.** For AIAP that places it
between Agents (6) and MCQ 1 (7) — a break immediately before the first
assessment.

| Wk | Topic | Lab | Needs a key |
|---|---|---|---|
| 1 | Module Introduction | — | |
| 2 | AIAP Overview | `labs/setup/` | |
| 3 | Prompting | `labs/prompting/` | |
| 4 | RAG | `labs/rag/` | yes |
| 5 | MCP | `labs/mcp/` | yes |
| 6 | Agents | `labs/agents/` | |
| — | *Reading week* | — | |
| 7 | **MCQ 1 — 20%** | — | |
| 8 | CLI Coding Agents | `labs/cli-coding-agents/` | |
| 9 | BaaS | `labs/baas/` | yes |
| 10 | CI/CD | `labs/cicd/` | |
| 11 | Vibe Coding | `labs/vibe-coding/` | |
| 12 | **MCQ 2 — 20%** | — | |

**Project — 60%.** Brief published in week 2, due at the end of week 12.

Non-teaching week folders (`week-07-mcq1`, `week-12-mcq2`,
`week-06b-reading-week`) keep a `README.md` as their only tracked file. Git
does not track empty directories and the site's rows derive from these folder
names, so that README is load-bearing. MCQ question content lives in Moodle
only and never enters this repository.

### 6. The tutor brief places no restriction on the assistant

OOC's `CLAUDE.md` tells a student's assistant to coach but never to write a
lab solution. That rule is incoherent in a module whose subject *is*
AI-assisted programming, where several labs instruct the student to have an
agent build something.

So AIAP's brief says the opposite: **the assistant is a full collaborator.**
Refusing to assist would teach the reverse of the module's own thesis.

The integrity load moves entirely onto assessment design, which is where it
already sat: two in-person MCQs worth 40% combined, and a project worth 60%
that is defended in person. Neither rewards code a student cannot explain.

This is a deliberate trade with a real cost, recorded in *Honest limits*
below.

## Architecture

    weeks/week-NN-<topic>/slides.md   Marp deck — THE canonical lecture
    labs/<topic>/README.md + code     THE canonical labs
    project/brief.md                  THE canonical project brief
    practice/index.html + bank/*.json MCQ practice app
    module/module-overview.md         weekly topics and coverage
    scripts/*.py                      the gates and the site build
    themes/aiap.css                   one theme, every deck
    .devcontainer/                    Python 3.12 + Node 20 + gh CLI
    CLAUDE.md                         audience router

Public site: `danielcregg.is-a.dev/ai-assisted-programming`. The custom domain
is configured at user level, so project pages route automatically with no DNS
work.

Nothing generated enters git. The site deploys straight from the workflow via
`actions/upload-pages-artifact` and `actions/deploy-pages`, with no `gh-pages`
branch — the mistake that had grown OOC's repository to roughly a gigabyte
before it was removed.

### The devcontainer is not lean

OOC's devcontainer is a stock Java image with no extra features, because Java
is all its labs need. AIAP cannot do that: the BaaS lab is a FastAPI backend
with a React/TypeScript frontend, so Python and Node are both required, and
several labs drive the `gh` CLI.

One image covers all nine labs — Python 3.12 base, Node 20 feature, `gh` CLI
feature. Accepted cost: a slower cold start than OOC's. Rejected alternative:
per-lab devcontainers, which would fragment the student's workspace and defeat
the single-copy model.

### Secrets in labs

Three labs need live API access (RAG, MCP, BaaS). The rules:

- `.env.example` ships; `.env` is gitignored and never committed.
- Students supply their own free-tier keys; each lab README says which and how
  to get one.
- `safety_audit.py` blocks any credential-shaped string on every push.
- Lab code reads keys from the environment only — never a literal, never a
  default value, never a committed config file.

## The six gates

Every push runs all six. This is where the repository stops being a folder and
starts being infrastructure.

| Gate | Checks | Honest limit |
|---|---|---|
| `check_links.py` | Every relative link, image and `#anchor` in tracked Markdown resolves | External URLs are never fetched |
| `safety_audit.py` | Student identifiers, credential-shaped strings, misplaced file types | Deliberately conservative: prints anything it cannot prove safe |
| `build_index.py` | A teaching week with no deck or no lab fails the build | Weeks legitimately without a lab are named in `NO_LAB_WEEKS = {1, 7, 12}` |
| `verify_snippets.py` | Every fenced snippet in decks and lab READMEs parses | Parses, does not execute — see below |
| `verify_labs.py` | Every lab module imports; `pytest` runs where tests exist | 6 of 9 labs fully; key-dependent parts carry an explicit marker |
| `check_practice_bank.py` | Question shape, option counts, per-topic minimum | Bank is seeded, not complete, until decks convert |

### Why `verify_snippets.py` parses rather than compiles

OOC compiles every Java fence with `javac`, and that gate is the single most
valuable guarantee in a programming module: a lecture cannot ship code that
claims to work but doesn't.

AIAP has no equivalent, because its decks do not carry one language. They
carry Python, JSON, YAML and bash. But all four *parse*, even where they
cannot meaningfully run:

| Fence | Check | Why it earns its place |
|---|---|---|
| ` ```python ` | `ast.parse` | Syntax errors in a worked example |
| ` ```json ` | `json.loads` | **An MCP server config that does not parse is exactly the error that wastes a room's hour** |
| ` ```yaml ` | `yaml.safe_load` | The CI/CD deck is largely workflow files |
| ` ```bash ` | `bash -n` (syntax only, never executed) | Unbalanced quoting in a command students will paste |

The contract is the same as OOC's: a fence is either verified or carries an
explicit `<!-- no-parse -->` marker directly above it. Nothing is silently
unchecked. The marker is the point.

This is a weaker guarantee than `javac` and is described as such. It catches
malformed configuration and broken syntax; it does not catch a prompt that
returns nonsense or a retrieval pipeline that ranks badly. Those are what the
end-of-semester AI content review is for.

## Distribution

Students click **Use this template**, not *Fork*. A fork of a public repo can
never be made private, which would publish every student's lab work; the fork
network would also publish a list of everyone taking the module.

Both workflows are guarded with `if: github.repository == '<this repo>'`,
because a template copy has Actions **enabled** — unlike a fork — and would
otherwise run the site build and commit to the student's own README every
Monday.

Mid-semester corrections reach students two ways: the website is canonical and
redeploys on push, and `scripts/update-course-content.sh` copies current
lectures, lab instructions and README into their copy. It **copies files
rather than merging branches** — with unrelated histories `git merge` refuses
outright, and forcing it conflicts on every differing file. It compares each
file against the version the student last received, not their latest commit,
because students are told to commit their work. Files they have edited are
kept and reported.

## Never enters this repository

- Student personal data of any kind.
- Real assessment material — the live MCQ bank stays in Moodle with a private
  backup outside the repo. `Assessments/MCQs/…top-20251207.xml` in OneDrive is
  the live bank and must never be converted into the practice bank.
- Credentials of any kind, or pointers to where credentials live.
- Worked solutions or instructor guides.
- Bulk third-party material.

## Honest limits

- **The tutor brief is a default, not a lock**, and here it is a permissive
  default by choice. A student can have an assistant write their entire
  project. The defence is the in-person MCQs and project defence, not the
  configuration.
- **Snippet verification is parsing, not execution.** Weaker than OOC's
  `javac` gate, and 3 of 9 labs cannot be fully verified in CI without live
  API keys.
- **The prompting lab's autograder survives only locally.** The self-check
  command works; the Classroom-hosted score and badge do not.
- **The practice bank is one topic deep.** 25 prompting questions ship;
  the other eight topics are authored as their decks convert.
- **`LAB_OVERRIDES` and `PENDING_DECKS` are both escape hatches** in
  `build_index.py`, and each is a place the derived layout stops deriving.
  `PENDING_DECKS` must shrink to empty as decks convert; the build fails if
  a week is listed there *and* has a deck, so it cannot rot silently.
- **Content ages fast.** These decks are from 2025 and the field has moved.
  Week-by-week conversion is also a refresh, which is a benefit, but it means
  the repository is incomplete for most of the semester.
- **A file a student edits stops updating.** Their work wins, but someone who
  annotates a lab README never receives later corrections to it.
- **It is GitHub-shaped.** Codespaces, Actions and Pages do real work here.
- **The devcontainer is heavier than OOC's** and will cold-start slower.

## Build order

1. Repository skeleton, `.gitignore`, `package.json`, devcontainer, `.vscode`.
2. The gate scripts and the site build.
3. Lab migration, solutions held back.
4. `themes/aiap.css`, `CLAUDE.md`, `README.md`, `project/brief.md`.
5. Week 1 deck converted from PowerPoint as the proof deck.
6. Practice app shell and seed bank; workflows.
7. All six gates pass locally — **before** anything reaches GitHub.
8. Create and push `danielcregg/ai-assisted-programming`; verify CI and site.
9. Create the private solutions repository.
