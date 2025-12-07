import re
import pandas as pd
from typing import Dict, List
from src.config import TECHNICAL_SKILL_ALIASES, SOFT_SKILL_ALIASES

def extract_soft_skills(text: str) -> set[str]:
    text_l = text.lower()
    found = set()
    for pattern, canonical in SOFT_SKILL_ALIASES.items():
        if pattern in text_l:
            found.add(canonical)
    return found


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


def build_skill_regex(alias_dict):

    all_aliases = []
    for aliases in alias_dict.values():
        all_aliases.extend(aliases)

    all_aliases = sorted(set(a.lower() for a in all_aliases), key=len, reverse=True)

    escaped = []
    for a in all_aliases:
        if a in {"c++", "c#", "c/c++"}:
            # Special handling: do NOT wrap with word boundaries
            escaped.append(re.escape(a))
        else:
            escaped.append(r"\b" + re.escape(a) + r"\b")

    pattern = "(" + "|".join(escaped) + ")"
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


    
