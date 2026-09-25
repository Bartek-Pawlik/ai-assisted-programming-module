"""A practical email-address validator."""

import re


_EMAIL_PATTERN = re.compile(
    r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@"
    r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+$"
)


def validate_email(address: str) -> bool:
    """Return whether address has a practical email-address format."""
    if len(address) > 254 or ".." in address:
        return False
    return bool(_EMAIL_PATTERN.fullmatch(address))
