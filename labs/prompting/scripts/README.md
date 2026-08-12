# Scripts Directory

This directory contains helpful scripts for the lab:

## 🎯 `run_and_grade.py`
**Main script for checking your progress**

Run this anytime to see:
- Your current score (0-100)
- Which tasks are complete/incomplete
- What you need to do next

```bash
python scripts/run_and_grade.py
```

**Note:** This script generates `pytest-report.json` and `autograde/` files automatically. These are temporary files and should **not** be committed to git (they're in `.gitignore`).

## 🔧 `setup_check.py`
**Environment troubleshooting script**

Run this if you're having any issues with the lab environment:

```bash
python scripts/setup_check.py
```

It will:
- Check if Python and pip are working
- Install missing packages automatically
- Verify the lab directory structure
- Give you specific instructions to fix any problems

## 📁 Generated Files (Don't Commit These)

The scripts automatically create these files:
- `pytest-report.json` - Test results in JSON format
- `autograde/grading-summary.json` - Scoring breakdown
- `.pytest_cache/` - Pytest cache directory

These are already in `.gitignore` and will be ignored by git.

## Quick Start for Students

1. **First time setup**: The devcontainer should handle everything automatically
2. **Check your progress**: `python scripts/run_and_grade.py`
3. **Having issues?**: `python scripts/setup_check.py`

That's it! Focus on the lab tasks, not the environment setup.