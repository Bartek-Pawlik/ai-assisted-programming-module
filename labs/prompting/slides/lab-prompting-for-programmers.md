---
marp: true
layout: title
class: center, middle
---
# Prompting for Programmers Lab
### From vague asks to reproducible results
Duration: ~90 minutes

---
## Learning Objectives
- Mental model: why vague prompts fail
- SPEC recipe application
- Constraints & Non-Goals
- Clarifying questions strategy
- Persona, Chain-of-Thought, Few-Shot
- Tests-first + Patch/Diff
- Instruction hierarchy & limitations

---
## Schedule (High-Level)
| Segment | Minutes |
|---------|---------|
| Warm-Up | 10 |
| SPEC Drill | 15 |
| Constraints + Questions | 15 |
| Persona + CoT | 15 |
| Few-Shot | 10 |
| Tests + Diff | 10 |
| Context + Limits | 10 |
| Reflection | 5 |

---
## SPEC Framework
| S | Specific Goal |
| P | Programming Language/Tool |
| E | Example (I/O) |
| C | Constraints |

Prompt skeleton:
```
Task: ...
Language/Files: ...
Example: input -> output
Constraints: ...
Return: (format)
```

---
## Bad vs Good Prompt
Bad: "Write a function to get second biggest number"

Better (SPEC):
```
Write a Python function second_largest(nums: list[int]) -> int
Return the second largest UNIQUE integer.
Example: [5,1,5,2] -> 2
Constraints:
- Raise ValueError if <2 unique numbers
- No sorting entire list more than once
Output: only the function code.
```

---
## Constraints & Non-Goals
Constraints focus scope.
Non-Goals prevent scope creep.

Example:
```
Constraints:
- Use existing slugify util style
- No new dependencies
Non-Goals:
- Do not add unicode normalization
- Do not refactor other helpers
```

---
## Clarifying Questions
Ask before coding:
- Scope? Success metric?
- Performance target?
- Backward compatibility?
- Security or compliance constraints?
- Preferred output format?

Template:
```
Before implementation, clarify:
1. Acceptance criteria?
2. Metrics / perf target?
3. Non-goals?
4. Files not to touch?
5. Output format preference?
```

---
## Persona Pattern
Generic: "Review my code"

Persona:
```
Act as a senior Python + security engineer.
Review for correctness, performance, security, readability.
List issues by category.
Suggest improved version.
```

---
## Chain-of-Thought
Add: "Think step by step before final answer"
Use for reasoning, debugging, verifying logic.

Guardrail: Ask for a short summary after long reasoning.

---
## Few-Shot Prompting
Provide 2–3 IN→OUT examples.
Lock in format, separators, ordering.

Use when: strict output JSON, transformation tasks, style imitation.

---
## Tests-First + Patch/Diff
1. Write minimal failing tests.
2. Prompt: "Implement only what's required to pass these tests. Output file content only."
3. For improvements: request unified diff.

Benefits: prevents overbuild, easier review.

---
## Instruction Hierarchy
1. Repo / policy files
2. File conventions
3. Explicit task prompt
4. Inline comments
5. Model defaults

If conflict: explain deviation.

---
## AI Limitations & Defenses
| Risk | Defense |
|------|---------|
| Hallucinated APIs | Ask for citation / confirm |
| Overconfidence | Require reasoning summary |
| Scope creep | Explicit Non-Goals |
| Hidden complexity | Tests-first |
| Style drift | Provide file path & style note |

---
## Reflection Prompts
1. Constraint success story
2. Most effective pattern
3. Hallucination caught / detection method
4. Instruction hierarchy use
5. Two new habits

---
## Final Reminder
Good prompting = disciplined specification.
Iterate, save prompts, reuse winners.

🚀 Happy Prompting!
