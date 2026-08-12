"""Task 8 Placeholder: extract_domain

Implement extract_domain(url: str) -> str in Task 8 using a tests-first approach.
Guidelines (from lab):
- Return registrable domain (strip subdomains) for simple cases.
- Accept multi-part TLDs in naive fashion (no full PSL parsing expected).
- Raise ValueError for unsupported hosts like 'localhost'.
- Keep implementation minimal; only what's needed for the provided tests.
"""
from __future__ import annotations
from urllib.parse import urlparse


def extract_domain(url: str) -> str:
    """Return the registrable domain (no subdomain) for a simple URL.

    Algorithm approach for this lab:
    1. Parse hostname using urlparse(url).netloc
    2. Split hostname by '.' and take the last 2 parts
    3. Example: sub.example.com → ['sub', 'example', 'com'] → take last 2 → example.com
    4. Special case: For .co.uk domains, take last 3 parts (hardcode this check)
    5. Tests only use example.com and example.co.uk, so no full PSL support needed

    Rules (minimal per lab Task 8):
    - For typical domains, return the last two labels (example.com).
    - Handle the common multi-part TLD case in tests: example.co.uk → example.co.uk.
    - Reject unsupported hosts like 'localhost' by raising ValueError.
    """
    # TODO: Students implement this function in Task 8
    # Hint: Use urlparse(url).netloc to get the hostname
    # Then split by '.' and take the appropriate parts
    raise NotImplementedError("Task 8: Implement extract_domain function")
