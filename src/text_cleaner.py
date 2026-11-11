
import re

def clean_text(text: str) -> str:

    # Remove null characters
    text = text.replace("\x00", " ")

    # Normalize spaces and tabs
    text = re.sub(r"[ \t]+", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove unwanted whitespace
    text = text.strip()

    return text
