# CLAUDE.md — how to work in this repo

Source-of-truth repo for the AI-Assisted Programming module (ATU, semester
1). Editable sources are Markdown, Python, TypeScript, JSON and HTML.

## First: whose repo is this, yours or a student's?

This file is read by two different people's assistants, and they need
different things. Work out which you are before doing anything.

**Check whether `CLAUDE.local.md` exists in the repo root.**

- **It exists → you are working with the module owner (Daniel).** He
  maintains this module. Everything below applies: the map, the
  conventions, the editing rules. `CLAUDE.local.md` carries his private
  operational context — read it.
- **It does not exist → you are almost certainly helping a STUDENT on
  their own copy.** Read the next section and follow it instead. Do not
  restyle decks, "fix" conventions, run the build scripts, or edit course
  content: their copy exists to hold their lab and project work, and the
  current instructions always live on the module site.

## If you are helping a student

**Help them. Fully. This module is about working with AI assistants, and
an assistant that refuses to assist would be teaching the opposite of the
syllabus.**

That is a deliberate decision by the module owner, and it is different
from the sibling Object-Oriented Computing repo, where you are told never
to write a lab solution. Here you may write code, debug, refactor,
explain, and pair on the project. There is no exercise you must decline.

The integrity load sits on assessment design instead, which is where it
belongs: two **in-person** MCQs worth 20% each, and a 60% project the
student must **present and defend**. Neither rewards code nobody
understands.

**So the useful thing you can do is make sure they understand it.** Not by
withholding — by teaching while you help:

- When you write something non-obvious, say why that approach and what the
  alternatives were.
- Prefer the smallest change that works, and name what it changed.
- When they paste an error, explain what it *means* before fixing it.
- Offer to quiz them on what you just wrote together. The MCQs are drawn
  from lecture and lab material, and the project is defended out loud.
- If they ask for a whole feature, build it — then walk them through it.

**Where the content is.** Lectures: `weeks/week-NN-<topic>/slides.md`
(Marp markdown — the teaching is in the prose, the fenced code, and the
`<!-- Speaker notes: ... -->` comments). Labs:
`labs/<topic>/README.md` beside the code the student edits. A rendered,
easier-to-read version of everything is at
https://danielcregg.is-a.dev/ai-assisted-programming/.

**Their work is theirs.** Edit the files they are working in. Leave decks,
scripts, workflows and the practice bank alone.

**Keys.** Three labs (`rag`, `mcp`, `baas`) need the student's own free
API key. Put it in a `.env` (gitignored) and read it from the environment
— never a literal in code, never a committed config file. If you see a key
in a file that is about to be committed, say so loudly.

## Map

- `weeks/week-NN-<topic>/slides.md` — Marp deck, THE canonical lecture.
  Week folders hold the lecture only; labs live under `labs/`.
- `labs/<topic>/` — THE canonical labs: `README.md` (the instructions
  students follow) plus starter code. Students copy the repo from the
  template and work here; a devcontainer provides Python 3.12, Node 20 and
  the `gh` CLI in one image (heavier than a single-language image, because
  `labs/baas` is a FastAPI backend WITH a React/TypeScript frontend).
  The repo is a TEMPLATE, not a fork source: a fork of a public repo
  cannot be made private, which would publish every student's work and
  list the class on the fork network. Workflows are guarded with
  `if: github.repository == '<this repo>'` because a template copy has
  Actions ENABLED (a fork does not) and would otherwise run this CI, and
  in `current-week.yml`'s case commit to the student's own README.
- **Labs are addressed by TOPIC, never by week number.** Week numbers move
  between years — this module went from 13 weeks to 12 — and student
  instructions should not follow them. The week number appears only in
  README's schedule table. `build_index.py` maps week folder → lab folder
  by topic slug, with `LAB_OVERRIDES` for the single week (week 2:
  overview lecture, setup lab) where the two names genuinely differ.
- `weeks/week-07-mcq1/`, `weeks/week-12-mcq2/` and
  `weeks/week-06b-reading-week/` — non-teaching weeks. Their `README.md`
  is the ONLY tracked file in each folder, so it is load-bearing: git does
  not track empty directories, and `build_index.py` derives the site's MCQ
  and reading-week rows from these folder names. Deleting the README
  deletes the row. MCQ question content lives in Moodle only — never
  commit it here.
- `project/` — the 60% project brief, rubric and AI-usage template. This
  is canonical; the `aiap-project-template` org repo is only a starter
  that links back here.
- `practice/` — the MCQ practice web app (`index.html`, self-contained
  vanilla JS) plus its bank (`bank/<topic>.json`). Bank questions are
  PRACTICE questions authored from the decks and labs — never the real
  Moodle assessment bank.
- The site is PUBLIC: https://danielcregg.is-a.dev/ai-assisted-programming/.
  Treat everything here as publishable: anything pushed is live within
  minutes, and speaker-note comments ship inside the rendered HTML where
  anyone can read them.

## Deck conversion is in progress

Lectures are being converted from PowerPoint week by week, ahead of the
week they are taught. The originals live in the module owner's OneDrive,
not here.

`PENDING_DECKS` in `scripts/build_index.py` lists the weeks not yet
converted; they render as marker rows on the site instead of broken links.
**Delete a week from that list the moment its `slides.md` lands** — the
build fails if a week is in both places, deliberately, because a converted
deck hidden behind a "pending" row is the same failure as a missing one.

## Conventions (guaranteed repo-wide)

- Folder/file names: kebab-case, no spaces.
- Every `slides.md` starts with YAML frontmatter: `title`, `week` (int),
  `topic` (kebab slug), `type` (`lecture`), `source` (`authored`),
  `marp: true`, `theme: aiap`, `paginate`. Lab READMEs carry no
  frontmatter — they are read as plain markdown on GitHub and on the site.
- Slides are separated by `---` on its own line; slide 1 uses `#`, the rest `##`.
- All decks use `themes/aiap.css` — edit the theme to restyle every deck at
  once. Per-slide classes via `<!-- _class: ... -->`: `lead` (title),
  `cols` (2-column bullets), `grid2`, `logos`, `dense`, `centered-table`,
  `side`, `code-sm`/`code-xs`. Kicker lines use
  `<span class="kicker">// ...</span>` (requires the workflow's `--html`).
- Bullet markers carry meaning: `* ` = fragmented (revealed one per
  keypress in the HTML presentation), `- ` = shown immediately. Fragment
  build-up slides; leave reference slides (agendas, summaries, tables)
  immediate.
- Speaker notes live in `<!-- Speaker notes: ... -->` comments at the TOP
  of the slide, straight after the `---`. A note carries what the slide
  does NOT show: elapsed time and tempo, **the misconception** (the
  specific wrong answer students give and the faulty model behind it),
  the slide's weight, and what it links to. Never restate the slide's own
  bullets. Notes **ship inside the rendered HTML** and are readable by
  anyone viewing source, so write them publishable: nothing about
  individual students.
- Decks are SELF-CONTAINED and reusable: never reference other weeks or
  the module schedule. Exempt: title-slide kickers, frontmatter `week:`,
  and week-01's module-logistics act.

## The gates

Six run on every push. Before any push, all must pass:

    python scripts/safety_audit.py        # credentials, student data, bad paths
    python scripts/check_links.py         # every relative link and anchor resolves
    python scripts/verify_snippets.py     # every fenced snippet parses
    python scripts/verify_labs.py         # lab code compiles; tests where possible
    python scripts/check_practice_bank.py # practice bank is well-formed
    python scripts/build_index.py build   # week <-> deck <-> lab structure holds

- `verify_snippets.py` is this repo's replacement for OOC's `javac` gate.
  There is no single language to compile here, so it PARSES: `ast.parse`
  for python, `json.loads`, `yaml.safe_load`, and `bash -n` (syntax only,
  never executed). A deliberately-broken snippet is skipped with
  `<!-- no-parse -->` on the line directly above its fence. **The marker
  is the point** — a fence is either verified or explicitly declared
  unverifiable, and nothing is silently unchecked.
- `verify_labs.py` compiles every lab `.py` and runs pytest where it can.
  `NEEDS_KEY` names the three labs (rag, mcp, baas) that cannot be
  verified beyond syntax without live credentials, and it prints that
  limit on every run rather than letting a green tick imply otherwise.
  `PLACEHOLDER_TESTS` names test files that are student scaffolding and
  are *expected to fail*; if one starts passing, a worked solution has
  reached the public repo and the gate says so.
- `check_links.py` matters more here than in OOC: the lab READMEs run
  10k–30k characters with their own tables of contents, and they arrived
  by migration from nine separate Classroom repos.

## Never commit

- Student personal data of any kind (names, IDs, grades, submissions).
- **Worked solutions or instructor guides.** They live in the private
  `ai-assisted-programming-labs-solutions` repo. This boundary carries
  more weight here than in OOC, because the tutor brief above places no
  restriction on the assistant — the repo split is the only thing between
  a student and an answer key.
- **Credentials of any kind.** Only `.env.example` may be tracked; every
  other `.env*` is gitignored and the audit rejects it.
- **Moodle enrolment passwords.** The week-01 deck deliberately says the
  group passwords are given out verbally: the deck is published on a
  public website.
- Real assessment material — the live MCQ bank stays in Moodle.
- Bulk third-party materials.

## Local preview (before committing)

    npm install          # once per machine — the marp-cli version pinned in
                         # package.json, the same one CI installs. There is no
                         # committed lockfile: CI uses `npm install -g <pinned>`
                         # and never reads one.
    npm run preview      # live server over weeks/ -> http://localhost:8080
    npm run export:intro # one deck straight to build/…/slides.pdf

After editing a deck's layout, re-render and check nothing overflows the
720px slide — content that spills is silently cropped in the PDF.
