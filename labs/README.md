# Labs

Nine labs, one folder each. Every folder has a `README.md` with the
instructions and the code you work in.

## Before you start

Sign up for the **[GitHub Student Developer Pack](https://education.github.com/pack)**
if you have not already. It is free for verified students, and it gives
you the **Copilot Student plan** — the editor assistant and the terminal
agent these labs use — and Pro-level Codespaces. Verification can take a
few days, so do it before the first lab rather than during it.

Use your real name on your GitHub account. You will be sending links to it
all semester, and it is the account an employer will look at.

## Getting your own copy

1. On the module repo, click **Use this template → Create a new
   repository**. Name it anything; **make it Private** — it's your work.
2. On *your* repo: **Code → Codespaces → Create codespace**.
3. The devcontainer gives you Python 3.12, Node 22 and the `gh` CLI. There
   is nothing to install.
4. Open the lab folder for this week and follow its README.

Don't *Fork*. A fork of a public repo can never be made private, so your
work would be world-readable, and the fork network would publish a list of
everyone taking the module.

Stop your Codespace when you finish for the day (it also stops itself
after half an hour idle). The free allowance is generous, not infinite.

## The labs

| Week | Lab | What you build | Needs |
|---|---|---|---|
| 2 | [setup](setup/) | Your environment, verified | |
| 3 | [prompting](prompting/) | SPEC prompts, personas, chain-of-thought, few-shot, context engineering | |
| 4 | [rag](rag/) | A retrieval pipeline — and when not to build one | a free API key, for the generation half |
| 5 | [mcp](mcp/) | An MCP server and client, then your own | |
| 6 | [agents](agents/) | The ladder of autonomy: ask → edit → act | |
| 8 | [security](security/) | Break it, then find the break: injection, slopsquatting, prompt injection | |
| 9 | [cli-agents](cli-agents/) | A terminal coding agent, configured: instructions, commands, permissions | a sign-in (GitHub or Google) |
| 10 | [cicd](cicd/) | A GitHub Actions pipeline with AI in it | |
| 11 | [vibe-coding](vibe-coding/) | The same app three ways — then spec-first | |

There is no lab in the introduction week or in the two MCQ weeks; the
[schedule](../README.md#module-schedule) says which weeks those are. Each lab has a short Practical Assessment on Moodle, worth
4% and open for that lab's week.

## Labs that need a key or a sign-in

The RAG lab's generation half calls a hosted model and needs an API key;
the default is the Gemini API's free tier, and its README says where to
get one. Nothing else needs a key: the MCP lab's weather
server uses a free service without one, and the security lab runs
offline by design. The CLI agents lab needs you to sign in to a coding
agent with your GitHub or Google account — a sign-in, never a key in a
file.

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

It refreshes the lectures, the lab instructions, the README, the Codespace
configuration, and any lab starter file you have **not** changed — so a
fix to a lab you have not started yet reaches you too. A file you have
edited, created or deleted is always yours: it is kept, and the script
tells you so.

The same update also runs **in your repo on GitHub every night**, so you
may see a commit called *update course content* appear that you did not
make. That is expected. If `git push` is ever rejected because of it, run
`git pull` first, then push again.
