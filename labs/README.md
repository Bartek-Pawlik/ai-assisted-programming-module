# Labs

Nine labs in the schedule, one folder each, plus one optional folder.
Every folder has a `README.md` with the instructions and the code you
work in.

## Getting your own copy

1. On the module repo, click **Use this template → Create a new
   repository**. Name it anything; **you may make it Private** — it's your
   work.
2. On *your* repo: **Code → Codespaces → Create codespace**.
3. The devcontainer gives you Python 3.12, Node 22 and the `gh` CLI. There
   is nothing to install.
4. Open the lab folder for this week and follow its README.

Don't *Fork*. A fork of a public repo can never be made private, so your
work would be world-readable, and the fork network would publish a list of
everyone taking the module.

## The labs

| Week | Lab | What you build | Needs a key |
|---|---|---|---|
| 2 | [setup](setup/) | Your environment, verified | |
| 3 | [prompting](prompting/) | SPEC prompts, personas, chain-of-thought, few-shot, context engineering | |
| 4 | [rag](rag/) | A retrieval pipeline — and when not to build one | yes |
| 5 | [mcp](mcp/) | An MCP server and client, then your own | yes |
| 6 | [agents](agents/) | The ladder of autonomy: ask → edit → act | |
| 8 | [security](security/) | Break it, then find the break: injection, slopsquatting, prompt injection | |
| 9 | [cli-agents](cli-agents/) | A terminal coding agent, configured: instructions, commands, permissions | sign-in |
| 10 | [cicd](cicd/) | A GitHub Actions pipeline with AI in it | |
| 11 | [vibe-coding](vibe-coding/) | The same app three ways — then spec-first | |

There is no lab in weeks 1, 7 or 12 (week 1 is the introduction; 7 and 12
are the MCQs). Each scheduled lab has a short Practical Assessment on
Moodle, worth 4% and open for that lab's week.

**Optional:** [baas](baas/) — a FastAPI backend and React frontend on a
hosted database. It is extra material, outside the schedule and not
assessed, and it needs a free Firestore project.

## Labs that need an API key

Two scheduled labs need an API key (rag, mcp), and so does the optional
baas lab. Each README says exactly which key and how to get one — all have
a free tier. The cli-agents lab needs a sign-in instead (GitHub or
Google), never a key in a file.

**Never commit a key.** Put it in a `.env` file in the lab folder; `.env`
is gitignored, and the repo's safety audit will reject one if it ever gets
staged. Read it from the environment in code — never a literal, never a
default value.

```bash
cp .env.example .env   # then edit .env with your own key
```

## Running a lab's tests

Labs are self-contained projects. Install from inside the lab folder:

```bash
cd labs/cicd
pip install -r requirements.txt
python -m pytest
```

## If a lab is corrected mid-semester

The [live site](https://danielcregg.is-a.dev/ai-assisted-programming/labs/)
always shows the current instructions — read there if something looks
wrong. To pull corrections into your own copy:

- **Automatically** — it runs each time you open your Codespace.
- **A button** — *Terminal → Run Task → Update course content*.
- **One line** — `bash scripts/update-course-content.sh`.

It only ever touches lab instructions, lectures and the README. It never
touches code you wrote, and if you've edited a file it keeps your version
and tells you.
