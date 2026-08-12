#!/usr/bin/env python3
"""Check that the lab code students are handed is not broken.

Two levels, because this module's labs cannot all be verified to the same
depth and pretending otherwise would be the real failure:

  1. SYNTAX -- every .py under labs/ is byte-compiled. No dependencies, no
     network, no keys. Runs for all nine labs, always.

  2. TESTS -- where a lab ships tests, pytest runs them. Three labs need
     live API access (see NEEDS_KEY) and cannot pass in CI without secrets,
     so their tests are reported as SKIPPED rather than quietly dropped.

Point 2 is the honest limit of this gate and it is printed on every run: a
lab in NEEDS_KEY has had its syntax checked and nothing more. The rule is
the same one the safety audit follows -- state what was not verified rather
than let a green tick imply it was.

Run from the repo root:
    python scripts/verify_labs.py            # syntax + runnable tests
    python scripts/verify_labs.py --syntax   # syntax only (no pytest)

Exits 1 if anything fails to compile or a runnable test fails.
"""
import argparse
import py_compile
import subprocess
import sys
from pathlib import Path

LABS = Path("labs")

# Labs whose tests need live API access or a cloud project, so CI cannot run
# them without secrets. Their syntax is still checked. Keep this list SHORT
# and justified -- it is a list of things this gate does not guarantee.
NEEDS_KEY = {
    "rag": "embeddings API key",
    "mcp": "weather API key",
    "baas": "Firestore project credentials",
}

TEST_GLOBS = ("test_*.py", "*_test.py")


def lab_dirs() -> list[Path]:
    return sorted(p for p in LABS.iterdir() if p.is_dir()) if LABS.is_dir() else []


def python_files(lab: Path) -> list[Path]:
    return sorted(p for p in lab.rglob("*.py")
                  if "__pycache__" not in p.parts and "node_modules" not in p.parts)


def test_files(lab: Path) -> list[Path]:
    found: set[Path] = set()
    for pattern in TEST_GLOBS:
        found.update(p for p in lab.rglob(pattern)
                     if "__pycache__" not in p.parts
                     and "node_modules" not in p.parts)
    return sorted(found)


def compile_lab(lab: Path) -> list[str]:
    errors = []
    for path in python_files(lab):
        try:
            py_compile.compile(str(path), cfile=None, doraise=True)
        except py_compile.PyCompileError as e:
            first = str(e).strip().split("\n")[0]
            errors.append(f"{path.as_posix()}: {first}")
    return errors


def run_tests(lab: Path) -> tuple[bool, str]:
    """Run pytest for one lab. Returns (passed, summary line)."""
    r = subprocess.run(
        [sys.executable, "-m", "pytest", str(lab), "-q", "--no-header",
         "-p", "no:cacheprovider"],
        capture_output=True, text=True)
    tail = [ln for ln in (r.stdout or "").strip().split("\n") if ln.strip()]
    summary = tail[-1] if tail else "(no output)"
    # pytest exit 5 == "no tests collected", which is not a failure here:
    # test_files() found something pytest chose not to collect.
    return (r.returncode in (0, 5)), summary


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--syntax", action="store_true",
                    help="compile only; do not run pytest")
    args = ap.parse_args()

    labs = lab_dirs()
    if not labs:
        print("verify_labs: no labs/ directory — nothing to check")
        return 0

    failures: list[str] = []
    rows: list[tuple[str, int, str]] = []

    for lab in labs:
        name = lab.name
        errors = compile_lab(lab)
        failures.extend(errors)
        n_py = len(python_files(lab))

        if errors:
            rows.append((name, n_py, "COMPILE FAILED"))
            continue
        if args.syntax:
            rows.append((name, n_py, "syntax only (--syntax)"))
            continue
        if name in NEEDS_KEY:
            rows.append((name, n_py, f"tests SKIPPED — needs {NEEDS_KEY[name]}"))
            continue

        tests = test_files(lab)
        if not tests:
            rows.append((name, n_py, "no tests in this lab"))
            continue
        passed, summary = run_tests(lab)
        if passed:
            rows.append((name, n_py, f"tests passed — {summary}"))
        else:
            rows.append((name, n_py, f"TESTS FAILED — {summary}"))
            failures.append(f"{lab.as_posix()}: pytest failed — {summary}")

    width = max(len(r[0]) for r in rows)
    print("verify_labs:")
    for name, n_py, status in rows:
        print(f"  {name:<{width}}  {n_py:>3} .py  {status}")

    if NEEDS_KEY and not args.syntax:
        unverified = ", ".join(sorted(NEEDS_KEY))
        print(f"\n  NOT verified beyond syntax: {unverified} — these need "
              f"live credentials.\n  A green run does not mean their exercises "
              f"work end to end.")

    for line in failures:
        print(f"\n{line}", file=sys.stderr)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
