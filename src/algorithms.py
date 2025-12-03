from collections import Counter
from typing import List, Any


def mean(values: List[float]) -> float:
    """Vrátí aritmetický průměr seznamu hodnot."""
    if not values:
        raise ValueError("Seznam nesmí být prázdný.")
    return sum(values) / len(values)


def is_palindrome(text: str) -> bool:
    """Zjistí, zda je text palindrom (ignoruje mezery a velikost písmen)."""
    cleaned = "".join(ch.lower() for ch in text if not ch.isspace())
    return cleaned == cleaned[::-1]