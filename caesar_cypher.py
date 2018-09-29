"""Caesar Cypher"""

from string import printable
from typing import Callable, List

POOL = printable[:-3]

def caesar_cypher(cleartext: str, offset: int, pool: List[chr] = POOL) -> str:
    """Encode the cleartext with the Caesar Cypher Algorithm."""

    return "".join(
        map(
            lambda x: POOL[(POOL.find(x) + offset) % len(POOL)],
            cleartext
            )
        )

def curried_caesar_cypher(offset: int, pool: List[chr] = POOL) -> Callable[[str], str]:
    """Creates a function that encodes received cleartext with
    the Caesar Cypher Algorithm by a fixed offset.

    Useful with streams.

    Usage:
    >>> curried_caesar_cypher(5)("Hello!")
    "Mjqqt&"

    >>> f = curried_caesar_cypher(5)
    >>> f("Hello!")
    "Mjqqt&"
    """
    return lambda cleartext: caesar_cypher(cleartext, offset)
