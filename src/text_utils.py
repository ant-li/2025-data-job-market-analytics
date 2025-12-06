import re
import pandas as pd

def extract_skills(text: str, skill_list: list[str]) -> list[str]:
    """
    Extracts matched skills from a block of text using exact keyword matching.

    Parameters
    ----------
    text : str
        Job description or other free-form text.
    skill_list : list[str]
        List of skill keywords to search for.

    Returns
    -------
    list[str]
        List of skills found in the text.
    """

    if pd.isna(text):
        return []

    text = text.lower()
    found = []

    for skill in skill_list:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, text):
            found.append(skill)

    return found
