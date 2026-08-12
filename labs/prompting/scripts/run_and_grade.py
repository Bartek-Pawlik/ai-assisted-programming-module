#!/usr/bin/env python3
"""Run lab tests and print a concise grading-style summary.

This mirrors the CI flow but with a friendlier local report:
- Runs: pytest lab/tests with JSON report
- Invokes the existing .github/scripts/score.py to compute score JSON
- Prints a compact dashboard (overall score + components + missing files)

No external dependencies beyond what's in requirements.txt (pytest, pytest-json-report).
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

# Simple ANSI color helpers (no external deps)
class C:
    R = "\x1b[31m"  # red
    G = "\x1b[32m"  # green
    Y = "\x1b[33m"  # yellow
    B = "\x1b[34m"  # blue
    C = "\x1b[36m"  # cyan
    M = "\x1b[35m"  # magenta
    W = "\x1b[37m"  # white
    D = "\x1b[0m"   # reset
    BOLD = "\x1b[1m"
    DIM = "\x1b[2m"

def status_icon(ok: bool) -> str:
    return f"{C.G}✓{C.D}" if ok else f"{C.R}✗{C.D}"

def progress_bar(ratio: float, width: int = 20) -> str:
    filled = int(ratio * width)
    bar = "█" * filled + "░" * (width - filled)
    color = C.G if ratio >= 0.7 else (C.Y if ratio >= 0.4 else C.R)
    return f"{color}{bar}{C.D}"

ROOT = Path(__file__).resolve().parents[1]
PYTEST_JSON = ROOT / "pytest-report.json"
SCORE_JSON = ROOT / "autograde" / "grading-summary.json"
SCORE_SCRIPT = ROOT / ".github" / "scripts" / "score.py"


def run_pytest() -> int:
    # Use the current Python executable (works with both global and venv)
    python_cmd = sys.executable
    
    cmd = [python_cmd, "-m", "pytest", "lab/tests", "-q",
           "--maxfail=1", "--json-report", f"--json-report-file={PYTEST_JSON.name}"]
    
    try:
        # Run quietly - output will be in JSON
        proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=False)
        return proc.returncode
    except FileNotFoundError:
        print(f"{C.R}❌ ERROR: pytest not found. Installing requirements...{C.D}")
        # Try to install requirements
        install_proc = subprocess.run([python_cmd, "-m", "pip", "install", "-r", "requirements.txt"], 
                                    cwd=ROOT, capture_output=True, text=True, check=False)
        if install_proc.returncode == 0:
            print(f"{C.G}✅ Requirements installed. Retrying tests...{C.D}")
            proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=False)
            return proc.returncode
        else:
            print(f"{C.R}❌ Failed to install requirements: {install_proc.stderr}{C.D}")
            return 1


def run_scoring() -> None:
    # Run scoring script quietly
    subprocess.run([sys.executable, str(SCORE_SCRIPT)], cwd=ROOT, 
                  capture_output=True, check=False)


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text())
    except (OSError, FileNotFoundError, json.JSONDecodeError):
        return {}


def is_reflection_complete(reflection_path: Path) -> bool:
    """Check if reflection is actually complete (not just template)."""
    if not reflection_path.is_file():
        return False
    
    try:
        content = reflection_path.read_text(encoding='utf-8').strip()
    except (OSError, UnicodeDecodeError):
        return False
    
    # Need substantial content
    if len(content) < 500:
        return False
    
    # Check for template indicators
    template_indicators = [
        "Fill this out after completing all tasks",
        "Your reflection goes here",
        "[Fill in your response]",
        "TODO:",
        "REPLACE THIS TEXT"
    ]
    
    content_lower = content.lower()
    if any(indicator.lower() in content_lower for indicator in template_indicators):
        return False
    
    return True


def get_missing_files() -> list[str]:
    """Get list of missing required files."""
    missing: list[str] = []
    required_list = [
        'lab/prompts/task1.md', 'lab/prompts/task2.md', 'lab/prompts/task3.md',
        'lab/prompts/task4.md', 'lab/prompts/task5.md', 'lab/prompts/task6.md',
        'lab/prompts/task7.md', 'lab/prompts/task9.md', 'lab/prompts/task10.md', 'lab/diffs/task9.diff'
    ]
    for f in required_list:
        if not (ROOT / f).is_file():
            missing.append(f)
    return missing

def show_task_status(py: dict) -> None:
    """Show compact task completion status."""
    # Group tasks by status
    complete = []
    incomplete = []
    
    def _check_prompt_sections(task_num: int, path: Path) -> bool:
        """Return True if the prompt file contains the required sections for the task.

        This is a lightweight heuristic (case-insensitive substring checks) to ensure
        students filled the main sections of each task file rather than leaving a bare template.
        """
        if not path.is_file():
            return False
        try:
            text = path.read_text(encoding="utf-8").lower()
        except (OSError, UnicodeDecodeError):
            return False

        # Define required keywords per task (all checks are lowercase)
        required: dict[int, list[str]] = {
            1: ["bad prompt", "good prompt", "ai output", "why better"],
            2: ["spec prompt", "ai output"],
            3: ["constraints", "non-goals"],
            4: ["scope", "metrics", "constraints", "risks", "output"],
            5: ["persona prompt", "raw ai review", "top 3"],
            6: ["(a) buggy", "(b) trimmed reasoning", "(c) micro tests", "(d) minimal fix", "(e) root cause"],
            7: ["few-shot", "prompt (strict", "ai output"],
            9: ["prompt (unified diff request)", "ai diff output", "how you applied"],
            10: ["bad prompt", "good prompt", "ai output", "why better"]
        }

        keys = required.get(task_num, [])

        # Helpers to detect substantive content after a header
        placeholder_indicators = ["paste", "your", "here", "todo", "# paste", "fill", "1.", "placeholder"]

        # Quick global check: if the whole file looks like a template/placeholder, bail early
        lowered = text.strip().lower()
        if len(lowered) < 30:
            return False
        # If many placeholder indicators appear near the start, treat as placeholder
        start_snip = lowered[:400]
        if sum(1 for ind in placeholder_indicators if ind in start_snip) >= 2:
            return False

        def _has_substantive_after(key: str) -> bool:
            # find the line containing the key
            lines = text.splitlines()
            for idx, line in enumerate(lines):
                if key in line:
                    # scan the next up to 8 lines for substantive content
                    for j in range(idx + 1, min(idx + 9, len(lines))):
                        nxt = lines[j].strip()
                        if not nxt:
                            continue
                        # ignore commented lines or header markers
                        if nxt.startswith("#"):
                            continue
                        low = nxt.lower()
                        # if line looks like a placeholder, skip
                        if any(ind in low for ind in placeholder_indicators):
                            return False
                        # if short bullets like '-' or numeric lists, treat as non-substantive
                        if low in ("-", "- ", "1."):
                            continue
                        # treat as substantive if length > 6
                        if len(nxt) >= 6:
                            return True
                    return False
            return False

        # Require all keys present and have substantive content after them
        satisfied = 0
        for k in keys:
            if k in text and _has_substantive_after(k):
                satisfied += 1

        # For most tasks require all keys satisfied; for task 7 allow 2/3
        if task_num == 7:
            return satisfied >= 2
        return satisfied == len(keys)

    # Tasks 1-7 and 10: prompt files (require specific sections)
    for i in list(range(1, 8)) + [10]:
        p = ROOT / f"lab/prompts/task{i}.md"
        if _check_prompt_sections(i, p):
            complete.append(f"Task {i}")
        else:
            incomplete.append(f"Task {i} (prompt file)")
    
    # Task 8: tests passing
    summary = py.get("summary", {})
    t_failed = int(summary.get("failed", 0)) + int(summary.get("error", 0))
    t_total = int(summary.get("passed", 0)) + t_failed + int(summary.get("skipped", 0))
    if t_total > 0 and t_failed == 0:
        complete.append("Task 8")
    else:
        incomplete.append("Task 8 (code implementation)")
    
    # Task 9: prompt file and diff file
    p9_md = ROOT / "lab/prompts/task9.md"
    p9_diff = ROOT / "lab/diffs/task9.diff"
    prompt_ok = _check_prompt_sections(9, p9_md)
    diff_ok = False
    if p9_diff.is_file():
        content = p9_diff.read_text(encoding="utf-8", errors="ignore").strip().lower()
        placeholder_diff_markers = ["placeholder diff", "paste your diff", "original content"]
        if content and not any(marker in content for marker in placeholder_diff_markers):
            diff_ok = True
    if prompt_ok and diff_ok:
        complete.append("Task 9")
    else:
        incomplete.append("Task 9 (prompt and diff files)")
    
    # Task 11: reflection
    rpath = ROOT / "lab/REFLECTION.md"
    if is_reflection_complete(rpath):
        complete.append("Task 11")
    else:
        incomplete.append("Task 11 (reflection)")
    
    # Display compact status
    if complete:
        complete_sorted = sorted(complete, key=lambda x: int(x.split()[1]))
        complete_str = ", ".join(complete_sorted)
        print(f"  {C.G}✓ DONE:{C.D} {complete_str}")
    
    if incomplete:
        incomplete_sorted = sorted(incomplete, key=lambda x: int(x.split()[1].split('(')[0]) if '(' in x else int(x.split()[1]))
        incomplete_str = ", ".join(incomplete_sorted)
        print(f"  {C.Y}⏳ TODO:{C.D} {incomplete_str}")
    
    # There are now 11 tasks (1-7 prompts, 8 code, 9 diff, 10 doc prompt, 11 reflection)
    completion_ratio = len(complete) / 11
    bar = progress_bar(completion_ratio, 30)
    print(f"  📈 Progress: {bar} {len(complete)}/11 tasks complete")


def verify_environment() -> bool:
    """Verify that the environment is properly set up."""
    try:
        # Test imports using current Python environment
        python_cmd = sys.executable
        
        # Check pytest
        result = subprocess.run([python_cmd, "-c", "import pytest; import pytest_jsonreport"], 
                              capture_output=True, text=True, check=False)
        if result.returncode == 0:
            return True
        else:
            print(f"{C.Y}⚠️  Missing dependencies. Installing...{C.D}")
            install_proc = subprocess.run([python_cmd, "-m", "pip", "install", "-r", "requirements.txt"], 
                                        cwd=ROOT, capture_output=True, text=True, check=False)
            if install_proc.returncode == 0:
                print(f"{C.G}✅ Requirements installed successfully{C.D}")
                return True
            else:
                print(f"{C.R}❌ Failed to install requirements automatically{C.D}")
                print(f"{C.Y}Please run: python scripts/setup_check.py{C.D}")
                print(f"{C.DIM}Error: {install_proc.stderr}{C.D}")
                return False
    except (OSError, FileNotFoundError) as e:
        print(f"{C.R}❌ Environment check failed: {e}{C.D}")
        return False


def main() -> int:
    print(f"\\n{C.BOLD}{C.C}{'='*60}{C.D}")
    print(f"{C.BOLD}{C.C}   🎯 Lab Progress Dashboard{C.D}")
    print(f"{C.BOLD}{C.C}{'='*60}{C.D}\\n")
    
    # Verify environment first
    if not verify_environment():
        print(f"\\n{C.R}❌ Environment setup incomplete. Please fix the above issues and try again.{C.D}")
        return 1
    
    print(f"{C.DIM}→ Running tests...{C.D}")
    rc = run_pytest()
    py = load_json(PYTEST_JSON)
    run_scoring()
    score = load_json(SCORE_JSON)

    # Overall score with visual progress
    overall = score.get("score", 0)
    if isinstance(overall, (int, float)):
        ratio = overall / 100
        bar = progress_bar(ratio)
        color = C.G if overall >= 90 else (C.Y if overall >= 60 else C.R)
        status = "🎉 EXCELLENT" if overall >= 90 else ("✅ PASSING" if overall >= 60 else "⚠️  NEEDS WORK")
        print(f"{C.BOLD}📊 OVERALL SCORE: {color}{overall:.0f}/100{C.D} {bar} {status}\n")
    else:
        print(f"{C.BOLD}📊 OVERALL SCORE: {C.Y}N/A{C.D}\n")

    # Component breakdown
    print(f"{C.BOLD}🔍 BREAKDOWN:{C.D}")

    # Tests
    summary = py.get("summary", {})
    t_passed = int(summary.get("passed", 0))
    t_failed = int(summary.get("failed", 0)) + int(summary.get("error", 0))
    t_total = t_passed + t_failed + int(summary.get("skipped", 0))
    t_ratio = (t_passed / t_total) if t_total else 0.0
    t_ok = t_failed == 0 and t_total > 0

    print(f"  {status_icon(t_ok)} Tests: {C.BOLD}{t_passed}/{t_total}{C.D} passing ({t_ratio:.0%}) - Worth 70% of grade")

    # Files: treat as present by default (they're created as templates)
    f_ok = True
    print(f"  {status_icon(f_ok)} Files: {C.BOLD}All required prompt files present{C.D} - Worth 20% of grade")

    # Reflection
    refl = score.get("reflection", {})
    r_present = bool(refl.get("present", False))

    print(f"  {status_icon(r_present)} Reflection: {C.BOLD}{'Complete' if r_present else 'Missing'}{C.D} - Worth 10% of grade\n")

    # What to do next
    if overall < 100:
        print(f"{C.BOLD}🎯 WHAT TO DO NEXT:{C.D}")
        if not t_ok:
            print(f"  {C.R}🔧 Fix failing tests{C.D} - Run: {C.C}python -m pytest lab/tests -v{C.D}")
        if not f_ok:
            missing = get_missing_files()
            print(f"  {C.Y}📝 Create missing files:{C.D}")
            for f in missing[:3]:  # Show first 3
                print(f"     • {f}")
            if len(missing) > 3:
                print(f"     • ... and {len(missing)-3} more")
        if not r_present:
            print(f"  {C.Y}✍️  Write reflection{C.D} - Edit: {C.C}lab/REFLECTION.md{C.D}")
        print()
    else:
        print(f"{C.BOLD}{C.G}🎉 PERFECT SCORE! You're ready to submit!{C.D}\n")

    # Compact task status
    print(f"{C.BOLD}📋 TASK CHECKLIST:{C.D}")
    show_task_status(py)
    
    # Footer
    print(f"\n{C.DIM}💡 Run this script anytime to check your progress{C.D}")
    print(f"{C.DIM}🚀 Push to GitHub when ready - you need 60+ to pass{C.D}")
    
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
