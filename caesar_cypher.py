"""Caesar Cypher"""

from string import printable
from typing import Callable

def caesar_cypher(cleartext: str, offset: int) -> str:
    """Encode the cleartext with the Caesar Cypher Algorithm."""

    return "".join(
        map(
            lambda x: printable[printable.find(x) + offset],
            cleartext
            )
        )

def curried_caesar_cypher(offset: int) -> Callable[[str], str]:
    return lambda cleartext: caesar_cypher(cleartext, offset)
