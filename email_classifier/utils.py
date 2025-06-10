import re

def clean_email_text(text):
    """
    Basic cleanup: remove extra whitespace and newlines.
    """
    return re.sub(r'\s+', ' ', text).strip()
