from pathlib import Path


def aged_receipts(root):
    """Receipts aged 2 to 8 weeks in the heat and UV chamber, one photo per week."""
    return sorted(Path(root).glob("week*/**/*.jpg"))
