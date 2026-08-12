[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=20849466)
<div align="center">

# Lab: Prompting for Programmers
### From vague asks to reproducible results (≈ 1.5 hours / 90 minutes)

💡 Goal: Learn to write clear, specific prompts that get reliable results from AI assistants.


[![Autograding Status](https://github.com/DanielCreggOrganization/w3-lab-prompting-danielcregg/actions/workflows/classroom.yml/badge.svg)](https://github.com/DanielCreggOrganization/w3-lab-prompting-danielcregg/actions/workflows/classroom.yml) ![Autograde Score](https://img.shields.io/badge/autograde-100%2F100-green)

</div>

---

## 🚀 START HERE (2 minutes)

**New to this lab?** Follow these steps:

1. ✅ You're already in Codespaces (dependencies auto-installed)
2. 💬 Open **Copilot Chat** in VS Code sidebar (should already be active)
3. 🧪 Test your setup: `python scripts/run_and_grade.py`
4. 📚 Read the [SPEC Framework](#-spec-framework-use-this-for-every-prompt) below
5. ▶️ Begin with [Task 1](#-task-1--bad-vs-good-prompt--10-min)

**Expected output from step 3**: You should see a score (likely 10/100 initially - that's normal!)

---

## 🔍 Learning Outcomes
By the end you will be able to:

- Explain (and apply) a mental model for why vague prompts fail.
- Use the SPEC recipe (Specific goal, Programming language/tool, Example I/O, Constraints) to shape outputs.
- Frame constraints vs. non-goals to prevent scope creep.
- Ask clarifying questions before writing code.
- Apply Persona, Chain‑of‑Thought, and Few‑Shot prompting patterns intentionally.
- Prompt tests‑first and request patch/diff style changes.
- Provide repository context + instruction hierarchy to the AI.
- Identify AI limitations and defend against hallucinations.

---

## ⏱️ Time Guide (Suggested)
| Time | Task | What You'll Do |
|------|------|----------------|
| 10 min | Task 1 | Rewrite a bad prompt using SPEC |
| 15 min | Task 2 | Practice SPEC on "slugify titles" |
| 10 min | Task 3 | Add constraints and non-goals |
| 10 min | Task 4 | Ask clarifying questions first |
| 10 min | Task 5 | Use persona prompting for code review |
| 10 min | Task 6 | Chain-of-thought debugging |
| 10 min | Task 7 | Format control with examples |
| 10 min | Task 8 | Write tests first, then implement |
| 10 min | Task 9 | Request and apply a code patch |
| 10 min | Task 10 | Documentation prompt practice |
| 5 min | Task 11 | Reflect on what you learned |

**Focus on doing fewer tasks well rather than rushing through all of them.**

---

## 🧭 Lab Structure
All work for this lab lives under the `lab/` folder (already present in this template). Add files here as you complete each task.

```text
lab/
├─ prompts/           # One markdown file per task you authored (task1.md … task7.md)
├─ outputs/           # Optional: raw AI outputs you kept for reference
├─ code/              # Your code artifacts (e.g., domains.py for Tasks 8–9)
├─ diffs/             # Saved unified diffs from patch-style prompts (e.g., task9.diff)
├─ tests/             # Your pytest files (Task 8); run: python -m pytest lab/tests -q
└─ REFLECTION.md      # Task 11: written reflection; must be non-empty for full score
```

Notes:
- Keep commits small and task-scoped (ideally one task per commit).
- In `lab/prompts/*.md`, include the exact prompt you used and the accepted AI output.
- Don't add new dependencies; Python 3.11 + pytest are already set up in this environment.

---

## 🚀 Quick Start (Students)
- Open in Codespaces (or Python 3.11 locally). The dev container auto-installs requirements.
- Check progress anytime (friendly dashboard):
    - `python scripts/run_and_grade.py`
- Or run raw tests only:
    - `python -m pytest lab/tests -q`
- Create prompts under `lab/prompts/` (Tasks 1–7), implement Task 8 in `lab/code/domains.py`, save Task 9 diff in `lab/diffs/task9.diff`, and complete `lab/REFLECTION.md` for Task 11.

**Having environment issues?** Run: `python scripts/setup_check.py`

**Your Score:**
- Tests = 70% (Task 8 implementation)
- Required Files = 20% (Tasks 1–7 + Task 9 diff file)
- Reflection = 10% (Task 11 write-up)

---

## ✅ SPEC Framework (Use This For Every Prompt)
| Element | Question | Example |
|---------|----------|----------|
| **S**pecific Goal | What exactly do you want? | "Add a function to trim whitespace" |
| **P**rogramming Language | Which language/file? | "Python 3.11 in `utils/strings.py`" |
| **E**xample | Show input → output | "'  hello  ' → 'hello'" |
| **C**onstraints | What limits/rules? | "No new dependencies; keep existing spaces inside" |

---

## 📝 Complete Example: SPEC in Action

Let's see the SPEC framework applied to a real problem:

### Bad Prompt (Vague)
Write a function to remove duplicates from a list.

### Good Prompt (SPEC Applied)
**Task**: Write a Python function that removes duplicate values from a list while preserving the original order.

**Programming**:
- Python 3.11
- Function signature: `def remove_duplicates(items: list) -> list`

**Examples**:
- Input: `[1, 2, 2, 3, 1]` → Output: `[1, 2, 3]` (keeps first occurrence)
- Input: `[]` → Output: `[]` (empty list returns empty)
- Input: `['a', 'b', 'a']` → Output: `['a', 'b']` (works with any type)

**Constraints**:
- Preserve the order of first occurrences
- Don't modify the input list
- Don't use external libraries
- Handle any hashable type (int, str, tuple, etc.)

**Return**: Only the function code with a docstring. No explanation.

### AI Output (Copilot Response)
```python
def remove_duplicates(items: list) -> list:
    """Remove duplicate values while preserving original order.
    
    Args:
        items: List of hashable items
        
    Returns:
        New list with duplicates removed, preserving first occurrence order
    """
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
```

### Why This is Better
- ✅ **Specific goal**: "preserve original order" vs vague "remove duplicates"
- ✅ **Clear language/signature**: Return type and input type specified
- ✅ **Examples show edge cases**: Empty list, different types, order preservation
- ✅ **Constraints prevent bloat**: "Don't modify input" clarifies behavior

**This is just a reference example. Your Task 1 will use a different problem!**

---

## 🧪 Tasks Overview
Each task builds a different muscle. Capture the prompt you *gave* the AI plus the *final artifact* you accepted.

| # | Skill | Deliverable |
|---|-------|------------|
|1| Bad → Good prompt rewrite | `prompts/task1.md` |
|2| SPEC recipe expansion | `prompts/task2.md` + accepted AI output snippet |
|3| Constraints & Non‑Goals refinement | `prompts/task3.md` |
|4| Clarifying questions | `prompts/task4.md` |
|5| Persona pattern for code review | `prompts/task5.md` + improved review notes |
|6| Chain‑of‑Thought debugging | `prompts/task6.md` + reasoning steps |
|7| Few‑Shot formatting control | `prompts/task7.md` + transformed outputs |
|8| Tests‑First implementation | Tests + minimal passing code |
|9| Patch/Diff request + application | Saved diff in `diffs/task9.diff` + updated code |
|10| Documentation prompt practice | `prompts/task10.md` |
|11| Reflection & instruction hierarchy | `REFLECTION.md` |

Detailed instructions follow.

---

## 🥁 Task 1 – Bad vs Good Prompt (≈ 10 min)

**What to do:**
1. Write a bad prompt: "Write a function to get the second largest number from a list." (vague!)
2. Rewrite using SPEC framework (be specific!)
3. Ask AI with your SPEC prompt
4. Save the result

**Create:** `lab/prompts/task1.md` with this structure:
```md
Bad Prompt:
[your vague prompt]

Good Prompt (SPEC):
[your SPEC-formatted prompt]

AI Output (trimmed):
[the code AI gave you]

Why better:
- [reason 1]
- [reason 2]
```

---

## 🧱 Task 2 – Practice SPEC (≈ 15 min)

**Starting point:** "Need a small utility to slugify titles." (too vague!)

**What to do:**
1. Turn this into a complete SPEC prompt
2. Ask AI using your prompt
3. Save both prompt and result

**Ideas for your SPEC:**
- **S**pecific: What exactly should slugify do?
- **P**rogramming: Pick Python or JavaScript
- **E**xample: "Hello World!" → "hello-world"
- **C**onstraints: ASCII only? Lowercase? How to handle punctuation?

**Create:** `lab/prompts/task2.md` with your SPEC prompt and AI's response

**Bonus:** Ask for 2 simple tests in the same prompt

---

## 🚧 Task 3 – Add Constraints & Non-Goals (≈ 10 min)

**What to do:**
1. Take your Task 2 prompt
2. Add 3-5 constraints (what you DO want)
3. Add 3-4 non-goals (what you DON'T want)
4. Explain why each one helps

**Example constraints:**
- "No external packages"
- "Handle empty strings gracefully"
- "Maximum 50 characters output"

**Example non-goals:**
- "No unicode normalization"
- "Don't optimize for speed"
- "Don't handle HTML entities"

**Create:** `lab/prompts/task3.md` with your enhanced prompt + explanations

---

## ❓ Task 4 – Ask Questions First (≈ 10 min)

**Starting point:** "Improve performance of the report generator." (super vague!)

**What to do:**
1. Write 7+ clarifying questions in these categories:
   - **Scope:** What parts need improvement?
   - **Metrics:** How do we measure "performance"?
   - **Constraints:** What can't we change?
   - **Risks:** What could break?
   - **Output:** What format do you want?

2. After the questions, write a much better prompt

**Create:** `lab/prompts/task4.md` with your questions + refined prompt

---

## 🧑‍💻 Task 5 – Persona Pattern Code Review (≈ 10 min)

**What to do:**
1. Ask AI to review code as a senior Python developer
2. Get specific feedback on multiple dimensions
3. Capture and summarize the insights

**Given code (has multiple issues):**
```python
def join(items):
    result = ""
    for i in range(len(items)):
        result = result + items[i] + ","
    return result
```

**Issues present**: trailing comma, inefficient string concatenation, no type hints, no input validation, uses range(len()) anti-pattern.

Create a persona prompt that asks the AI (as a senior Python + security + style reviewer) for:
* Correctness issues
* Readability improvements
* Edge cases
* Potential security or injection concerns
* Suggested improved implementation

**Create:** `lab/prompts/task5.md` with the persona prompt, raw AI review (trimmed), and your top 3 improvement summary

---

## 🧠 Task 6 – Chain‑of‑Thought Debugging (≈ 10 min)

What is Chain‑of‑Thought debugging? Briefly: it's a structured, testable way to reason about bugs where you state short hypotheses, design tiny tests that rule those hypotheses in or out, and then apply the smallest code change that fixes the reproduced issue. The goal is focused, verifiable reasoning — not long essays.

Start with this tiny buggy snippet (copy-paste so everyone can reproduce quickly):

```python
# Buggy example: always appends a trailing comma and uses inefficient concatenation
def join(items):
    result = ""
    for i in range(len(items)):
        result = result + items[i] + ","
    return result
```

**At a glance:**
- Goal: Demonstrate structured debugging with minimal, testable reasoning.
- Produce: `lab/prompts/task6.md` containing (a) the buggy snippet or a precise bug description, (b) trimmed reasoning steps / top hypotheses, (c) 2–3 micro tests/checks, (d) the minimal fix (1–3 lines), and (e) a one‑paragraph root cause.
- Steps:
    1) Use the provided snippet or pick a small bug (10–20 lines) of your own.
    2) Ask AI for top hypotheses, 2–3 minimal tests, and the smallest possible fix (1–3 lines).
    3) Capture only the essential reasoning (bulleted).
    4) Record the tests and the minimal code fix/patch.
    5) Summarize the root cause in your own words.
- Acceptance: All five parts are present; fix is minimal and addresses the reproduced issue.

Note: If you want extra practice, pick your own small bug instead of the provided example. The provided snippet exists to make the exercise reproducible and lower the barrier to getting started.

Keep commits small & meaningful. Prefer one task per commit.

---

## 🧮 Task 7 – Few‑Shot Formatting Control (≈ 10 min)

Goal: Use few‑shot examples to force the AI to produce output in an exact format (e.g., CSV, JSON, Markdown table) without extra prose.

**What to do:**
- Provide 2–3 strict IN → OUT pairs that demonstrate the exact input and the exact desired output.
- Specify formatting rules (e.g., header row required, no trailing commas, order of fields, lowercase only).
- Include a "Do not include commentary" constraint to avoid extra text around the output.

**Deliverables:**
- `lab/prompts/task7.md` containing your final prompt and the accepted AI output snippet.

**Example sketch (CSV):**
```
Input lines:
    "Alpha:1", "Beta:2", "Gamma:3"

Output CSV (header required, exactly these columns: name,value; no extra spaces):
name,value
alpha,1
beta,2
gamma,3
```

**Constraints (example):**
- Output only the CSV (no code fences, no commentary).
- Lowercase names; keep numeric values as-is.
- Preserve input order.

---

## 🛠️ Prerequisites
* GitHub Codespaces (already provisioned) & Git tooling.
* An AI assistant (e.g., Copilot Chat / inline / terminal).
* Basic familiarity with JavaScript or Python (choose one and stay consistent per task unless stated otherwise).

---

## 🧪 Task 8 – Write Tests First (≈ 10 min)

**Goal:** Get AI to create a function, based on unit test requirements, that extracts the main domain from URLs

**What to do:**
1. **Write tests first** in `lab/tests/test_extract_domain.py`:
   - `https://sub.example.com/path` → `example.com`
   - `http://example.co.uk` → `example.co.uk`
   - `https://localhost` → should raise ValueError

**Algorithm Approach**:
For this lab, use a simplified domain extraction:
1. Parse hostname using `urlparse(url).netloc`
2. Split hostname by '.' and take the last 2 parts
3. Example: `sub.example.com` → split to `['sub', 'example', 'com']` → take last 2 → `example.com`
4. Special case: For `.co.uk` domains, take last 3 parts (you may hardcode this check)
5. The tests only use `example.com` and `example.co.uk`, so you don't need full PSL support

2. **Then ask AI to implement** `extract_domain(url: str) -> str` in `lab/code/domains.py`

3. **Use this exact prompt:**
   ```
   Implement only the code needed to make these tests pass.
   File: lab/code/domains.py
   Function: extract_domain(url: str) -> str
   Rules: No external dependencies, minimal code, raise ValueError for localhost
   Output: Just the code, no explanation
   ```

4. **Test it:** `python -m pytest lab/tests -q`

**At a glance:**
- Goal: Write tests first, then implement only what's needed to pass.
- Produce: `lab/tests/test_extract_domain.py` tests and `lab/code/domains.py` minimal implementation.
- Steps: Read tests → implement `extract_domain(url: str) -> str` using `urllib.parse.urlparse` → keep logic compact → raise `ValueError` on unsupported hosts.
- Acceptance: Provided tests pass locally; no new dependencies; minimal code.

---

## 🩹 Task 9 – Request a Code Patch (≈ 10 min)

**Goal:** Ask AI to improve your Task 8 code using a "diff" format

**What to do:**
1. Ask AI to add:
   - Input validation (reject empty strings)
   - A docstring
   - Keep everything else the same

2. **Important:** Ask for a "unified diff" format only (no explanations)

3. Save AI's diff output to `lab/diffs/task9.diff`

4. Apply the changes manually to `lab/code/domains.py`

5. **Test still works:** `python -m pytest lab/tests -q`

**Example prompt:** "Generate a unified diff to add input validation and docstring to extract_domain. Output only the diff."

---

## 📚 Task 10 – Documentation Prompt Practice (≈ 10 min)

**Goal:** Practice writing prompts for professional-quality documentation

**What to do:**
1. Take the provided function and write a SPEC-style prompt to generate NumPy-style docstring + brief README snippet.
2. Ask AI using your prompt.
3. Save the prompt and accepted AI output.

**Given function:**
```python
def compute_statistics(numbers: list[float]) -> dict:
    """Return a dictionary with keys: count, mean, median, stdev."""
    # minimal naive implementation
    import math
    n = len(numbers)
    if n == 0:
        return {"count": 0, "mean": 0.0, "median": 0.0, "stdev": 0.0}
    sorted_nums = sorted(numbers)
    mean = sum(numbers) / n
    median = sorted_nums[n//2] if n % 2 == 1 else (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    var = sum((x - mean) ** 2 for x in numbers) / n
    stdev = math.sqrt(var)
    return {"count": n, "mean": mean, "median": median, "stdev": stdev}
```

**Create:** `lab/prompts/task10.md` with your SPEC prompt and the AI's documentation output.

---

## 🔐 Task 11 – Write Your Reflection (≈ 5–10 min)

**Goal:** Think about what you learned

**Create:** `lab/REFLECTION.md` answering these 5 questions:

1. **Constraint Success:** Give one example where adding constraints prevented the AI from doing too much

2. **Best Pattern:** Which prompting technique worked best for you today? (SPEC, Persona, Chain-of-Thought, Few-Shot, Tests-First, or Patch/Diff)

3. **AI Mistakes:** Did you catch the AI making something up or getting something wrong? How?

4. **Information Sources:** What did you rely on most? (README, existing code, task instructions, etc.)

5. **Future Habits:** What 2 things will you do differently when prompting AI next time?

**Keep it short and honest!**

---

## 🧭 Instruction Hierarchy (Reference)
1. Repo-level / policy files (e.g., path rules, contribution guidelines)
2. File-level conventions & existing code structure
3. Explicit prompt task text
4. Inline comments / local hints
5. Model defaults / generic knowledge

If conflict: explain deviation rather than silently ignoring higher-order rules.

---

## ⚠️ AI Limitations (Defense Checklist)
| Risk | Mitigation Prompting Pattern |
|------|------------------------------|
| Hallucinated APIs | Ask: "Cite source or confirm if speculative" |
| Overconfidence | Request reasoning: Chain-of-Thought summary |
| Hidden complexity | Tests-first + minimal diff enforcement |
| Style drift | Provide file path + style constraints |
| Scope creep | Explicit Non-Goals section |

---

## 📦 Before You Submit
- [ ] All prompt files created: `lab/prompts/task1.md` through `task7.md` plus `task10.md`
- [ ] Task 8: `lab/code/domains.py` and `lab/tests/test_extract_domain.py`
- [ ] Task 9: `lab/diffs/task9.diff` saved and applied
- [ ] Task 10: `lab/prompts/task10.md` completed
- [ ] Task 11: `lab/REFLECTION.md` completed
- [ ] Tests pass: `python -m pytest lab/tests -q`
- [ ] Local check: `python scripts/run_and_grade.py` shows good score

---

## 🧮 Grading Rubric (100 pts)
| Category | Points | Criteria |
|----------|--------|----------|
| Prompt Quality (Tasks 1–3) | 20 | SPEC completeness, clarity, constraint usefulness |
| Clarifying Questions (Task 4) | 10 | Coverage, categorization, relevance |
| Advanced Patterns (Tasks 5–7) | 20 | Persona specificity, CoT utility, Few‑Shot precision |
| Tests‑First & Implementation (Task 8) | 20 | Tests meaningful, code minimal & correct |
| Patch/Diff Accuracy (Task 9) | 10 | Clean diff, only required changes |
| Reflection (Task 11) | 10 | Depth, insight, actionable habits |
| Professionalism | 10 | Structure, commit hygiene, reproducibility |

Bonus (up to +5): Additional defensibility (e.g., security check list, automated script to run tests) – may not exceed 100 overall.

---

## 💡 Quick Tips

**When you need to:**
- **Get specific answers:** "Before coding, ask 5 clarifying questions about..."
- **Keep it simple:** "Implement only what's needed for these tests to pass"
- **Get a code change:** "Return a unified diff only. No explanation."
- **Match existing style:** "Use the same formatting as in [filename]"
- **Prevent extra features:** "Non-Goals: Don't add X, Y, or Z"
- **See AI's thinking:** "Think step by step. Show your reasoning first"
- **Control format exactly:** Give 2-3 examples of exact input → output

---

## 🧪 Quick Local Test Instructions (Python example)
After creating tests in Task 8:
```bash
python -m pytest -q
```
If `pytest` not installed: `pip install pytest`.

---

## 🙌 Wrap Up

The goal is to **deliberately choose** the right prompting technique instead of guessing. Save your best prompts—you'll reuse them!

> "Good prompting is just clear specification."

Happy Prompting! 🚀

---

## 🆘 Troubleshooting

### Tests Failing

**Error: `ModuleNotFoundError: No module named 'pytest'`**
```bash
pip install -r requirements.txt
```

**Error: `ModuleNotFoundError: No module named 'lab'`**
- Ensure you're running from repo root: `python -m pytest lab/tests -q`
- Not from inside the `lab/` directory

**Tests fail: `NotImplementedError`**
- You haven't implemented `extract_domain` yet (that's Task 8!)
- Create placeholder files for Tasks 1-7 first to improve your score

### Copilot Not Responding

**Inline suggestions not appearing?**
- Check bottom-right status bar - should show Copilot icon
- Try: `Ctrl+Enter` (Windows) or `Cmd+Enter` (Mac) to manually trigger

**Chat panel empty?**
- Click Copilot icon in left sidebar
- Or: `Ctrl+Shift+I` (Windows) / `Cmd+Shift+I` (Mac)

### File/Folder Issues

**Can't find `lab/prompts/` directory?**
- It exists but may be collapsed in Explorer
- Or create it: `mkdir -p lab/prompts`

**Diff file format confusing?**
- Ask Copilot: "Explain this unified diff format"
- See example: [Git diff docs](https://git-scm.com/docs/git-diff)

### Task 8 Confusion

**Don't know where to start with `extract_domain`?**
- Read the algorithm hint in Task 8 carefully
- Start with: `from urllib.parse import urlparse`
- Print intermediate steps: `print(urlparse(url).netloc)`
- Build incrementally

**Still stuck? Ask Copilot:**
```
I need to implement extract_domain(url: str) -> str.
It should return 'example.com' from 'https://sub.example.com/path'.
Show me step-by-step how to:
1. Extract the hostname
2. Split it into parts  
3. Take the last 2 parts
```

### Grading Questions

**Score not updating after fixes?**
- Commit and push your changes
- Check Actions tab for latest run
- Badge updates automatically (may take 1-2 min)

**Score stuck at 10/100?**
- 10 = only reflection file exists
- Create prompt files (Tasks 1-7) for +20 points
- Implement Task 8 for +70 points

---

## 🔁 Check Your Progress

**Local (Fast):** `python scripts/run_and_grade.py`
- Shows overall score, which files are missing, which tests are failing
- Run this after each task to stay on track

**GitHub (Slower):** Check the Actions tab
- Green = passing, Red = failing
- Must score 60+ to pass
- Badge shows your current score

**Scoring Breakdown:**
1. **Tests (70%):** Does Task 8 code work?
2. **Files (20%):** Are all prompt files and diff present?
3. **Reflection (10%):** Did you write something in `REFLECTION.md`?

**Quick Fixes:**
- Tests failing? Fix your `extract_domain` function
- Files missing? Create placeholder files with basic content
- Low score? Run the local script to see exactly what's missing

---

## 📚 Key Terms
- **Artifact:** Any file you create (prompts, code, tests, diffs, reflection)
- **Trimmed AI Output:** The useful part of AI's response (not the full chat)
- **Minimal fix:** Smallest possible code change to solve the problem

---

## 🔧 Additional Troubleshooting

**Environment Issues?**
```bash
python scripts/setup_check.py
```
This will check and fix common setup problems automatically.

**Tests Not Running?**
- Make sure you're in the right directory: `cd /workspaces/aiap-w2-lab-prompting-aiap-labs-template`
- Check if pytest is installed: `python -m pytest --version`
- If missing, install: `pip install -r requirements.txt`

**Python Import Errors?**
- This lab uses Python 3.11 (pre-installed in Codespaces)
- If VS Code shows "Import could not be resolved" for pytest:
  - Check that VS Code is using `/usr/local/bin/python` as the interpreter
  - Try: Ctrl+Shift+P → "Python: Select Interpreter" → Choose `/usr/local/bin/python`
- Avoid creating virtual environments for this lab - use the global Python

**Score Not Updating?**
- Run the local checker: `python scripts/run_and_grade.py`
- Commit and push your changes to trigger GitHub grading
- Check the Actions tab for detailed results

**Files You Should NOT Commit:**
- `pytest-report.json` (auto-generated test results)
- `autograde/` directory (auto-generated scoring data)
- `.pytest_cache/` (pytest cache)

These files are already in `.gitignore` and will be ignored automatically.

**Need Help?**
1. Run `python scripts/setup_check.py` first
2. Check the Actions tab for specific error messages
3. Look at the specific test failures in the output

---

### Slide Deck
For a slide-friendly version of this lab, see: `slides/lab-prompting-for-programmers.md`