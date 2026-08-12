# Prompting Patterns Quick Reference

## When to Use What

| I need to... | Use this pattern | Jump to |
|--------------|------------------|---------|
| Get specific working code | SPEC framework | [Task 1-2](#) |
| Prevent AI from adding extra features | Constraints + Non-Goals | [Task 3](#) |
| Understand requirements before coding | Clarifying Questions | [Task 4](#) |
| Get expert-level feedback | Persona prompting | [Task 5](#) |
| Debug complex logic | Chain-of-Thought | [Task 6](#) |
| Control exact output format | Few-Shot examples | [Task 7](#) |
| Avoid over-engineering | Tests-First | [Task 8](#) |
| Make surgical code changes | Patch/Diff request | [Task 9](#) |

---

## SPEC Template (Copy & Modify)

**Task**: [One sentence: what exactly do you want?]

**Programming**:
- Language: [Python 3.11, JavaScript, etc.]
- Location: [file path or new file name]
- Signature: [function/class name and types]

**Examples**:
- Input: [concrete example] → Output: [expected result]
- Input: [edge case] → Output: [expected behavior]

**Constraints**:
- [Limit 1: e.g., "No external libraries"]
- [Limit 2: e.g., "Must handle empty input gracefully"]
- [Limit 3: e.g., "Max 20 lines of code"]

**Non-Goals (Don't do these)**:
- [Thing 1: e.g., "Don't add database caching"]
- [Thing 2: e.g., "Don't refactor existing code"]

**Return**: [Only the code | Only a diff | Code + 3 tests | etc.]

---

## My Top Prompts This Week

**Keep your winners here for reuse:**

### 1. [Prompt name]
[Paste your best prompt here]

**Why it worked**: [Note to self]

### 2. [Prompt name]
[Paste your best prompt here]

**Why it worked**: [Note to self]

### 3. [Prompt name]
[Paste your best prompt here]

**Why it worked**: [Note to self]

---

## Common Copilot Shortcuts

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Accept suggestion | `Tab` | `Tab` |
| Reject suggestion | `Esc` | `Esc` |
| Next suggestion | `Alt+]` | `Option+]` |
| Previous suggestion | `Alt+[` | `Option+[` |
| Open Chat | `Ctrl+Shift+I` | `Cmd+Shift+I` |
| Inline Chat | `Ctrl+I` | `Cmd+I` |

---

## Red Flags (AI Mistakes to Watch For)

- ❌ AI invents functions that don't exist (`urlparse.get_domain()`)
- ❌ AI adds dependencies you didn't ask for (`import beautifulsoup4`)
- ❌ AI writes 100 lines when 10 would work
- ❌ AI ignores your constraints (you said "no loops", it uses loops)
- ❌ AI formats output with extra commentary when you said "code only"

**Defense**: Always test the code. Re-prompt with stronger constraints if needed.

---

## Commit Message Templates

- `Complete Task 1: Rewrite vague prompt using SPEC`
- `Complete Task 8: Implement extract_domain with tests`
- `Fix Task 8: Handle localhost ValueError`
- `Complete Task 9: Apply docstring patch via diff`
- `Complete Task 10: Add reflection on prompting patterns`