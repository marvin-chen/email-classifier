import re

def clean_email_text(text: str) -> str:
    """
    Clean email text by removing unnecessary characters and normalizing whitespace.
    
    Args:
        text (str): Raw email text.
    
    Returns:
        str: Cleaned email text.
    """
    if not text:
        return ""
    # Remove extra whitespace and newlines
    text = re.sub(r'\s+', ' ', text.strip())
    # Remove common email signatures and boilerplate
    text = re.sub(r'--\s*Sent from.*$', '', text, flags=re.MULTILINE)
    return text