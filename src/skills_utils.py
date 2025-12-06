# import re
# import pandas as pd

# def extract_skills(text: str, skills: list[str]) -> list[str]:
#     """
#     Return a list of skills from `skills` that appear in `text`.
#     Handles 'r' as a special case to reduce false positives.
#     """
#     if pd.isna(text):
#         return []

#     s = str(text).lower()
#     found = []

#     for skill in skills:
#         skill_l = skill.lower()

#         if skill_l == "r":
#             # Special handling for 'r' language:
#             # - Not part of a longer word
#             # - Not followed by & or /
#             # Matches: " R ", "python, scala or R.", "R programming"
#             # Avoids: "R&D", "R/GA"
#             pattern = r"(?<![a-z0-9])r(?![a-z0-9&/])"
#         else:
#             pattern = r"\b" + re.escape(skill_l) + r"\b"

#         if re.search(pattern, s):
#             found.append(skill)

#     return found

import re
import pandas as pd
from typing import Dict, List
from src.config import TECHNICAL_SKILL_ALIASES


def build_alias_lookup(alias_dict: Dict[str, List[str]]) -> Dict[str, str]:
    """
    Convert canonical -> [aliases] into alias -> canonical lookup.
    All keys are lowercased for case-insensitive matching.
    """
    lookup: Dict[str, str] = {}
    for canonical, aliases in alias_dict.items():
        for alias in aliases:
            lookup[alias.lower()] = canonical
    return lookup


def build_skill_regex(alias_dict: Dict[str, List[str]]) -> re.Pattern:
    """
    Build one compiled regex that matches any skill alias in a case-insensitive way.
    """
    all_aliases: List[str] = []
    for aliases in alias_dict.values():
        all_aliases.extend(aliases)

    # Remove duplicates and sort by length (longer first to avoid partial overlaps)
    all_aliases = sorted(set(a.lower() for a in all_aliases), key=len, reverse=True)

    pattern = r"\b(" + "|".join(re.escape(a) for a in all_aliases) + r")\b"
    return re.compile(pattern, flags=re.IGNORECASE)


def extract_skills(text: str,
                             alias_lookup: Dict[str, str],
                             compiled_pattern: re.Pattern) -> List[str]:
    """
    Extract canonical technical skills from free text using alias lookup and compiled regex.

    Parameters
    ----------
    text : str
        Job description text.
    alias_lookup : dict
        Maps alias (lowercase) -> canonical skill.
    compiled_pattern : Pattern
        Regex built by build_skill_regex over all aliases.

    Returns
    -------
    list[str]
        Canonical skills found, in order of first appearance, without duplicates.
    """
    if pd.isna(text):
        return []

    s = str(text).lower()

    # Find all alias matches in the text
    matched_aliases = [m.group(1).lower() for m in compiled_pattern.finditer(s)]

    # Map aliases -> canonical and preserve order without duplicates
    seen = set()
    result: List[str] = []
    for alias in matched_aliases:
        canonical = alias_lookup.get(alias, alias)
        if canonical not in seen:
            seen.add(canonical)
            result.append(canonical)

    return result


    
