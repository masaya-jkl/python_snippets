"""Caesar Cypher"""

from string import printable

def caesar_cypher(cleartext: str, offset: int) -> str:
    """Encode the cleartext with the Caesar Cypher Algorithm."""

    return "".join(
        map(
            lambda x: printable[printable.find(x) + offset],
            cleartext
            )
        )
