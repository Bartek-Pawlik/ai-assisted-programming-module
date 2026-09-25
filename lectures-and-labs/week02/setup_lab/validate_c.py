"""A straightforward email-address validator."""


def validate_email(address: str) -> bool:
    """Return whether address has one local part and a dotted domain."""
    if len(address) > 254 or address != address.strip():
        return False

    local_part, separator, domain = address.partition("@")
    if not separator or not local_part or not domain:
        return False
    if "@" in domain or ".." in address:
        return False

    domain_parts = domain.split(".")
    return all(part for part in domain_parts)