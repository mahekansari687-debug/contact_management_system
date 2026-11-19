import re


def validate_email(email):
    """Check whether email format is valid."""
    pattern = r'^[\w.-]+@[\w.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def format_phone(phone):
    """Remove spaces and special characters from phone number."""
    return re.sub(r'\D', '', phone)