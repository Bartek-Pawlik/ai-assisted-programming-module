# Task 10 — Documentation Prompt Practice (≈ 10 min)

**Goal:** Practice writing SPEC-style prompts to produce professional
NumPy-style docstrings and a short README snippet for a given function.

**What to do:**

1. Write a SPEC prompt that asks the AI to produce a NumPy-style docstring
   for the provided function and a brief README section that explains the
   function's purpose and usage.
2. Ask the AI and capture the accepted output (trimmed to the docstring +
   README snippet).
3. Save the prompt you used and the AI's accepted output in this file.

## Given function

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

## Bad Prompt

# Paste the vague prompt you started with (e.g., "Document this function")

## SPEC Prompt (for docs)

# Paste the SPEC-style prompt you used to request a NumPy-style docstring
# plus a README snippet

## AI Output (trimmed)

# Paste the docstring/README snippet the AI produced and you accepted
