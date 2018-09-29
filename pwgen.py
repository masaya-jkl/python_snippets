import secrets
import string
from typing import List

POOL = string.printable[:-6] # -3 to include basic whitespace characters

def create_key(size: int, pool: List[chr] = POOL) -> str:
    """(int) -> str
    Returns n random chars and concatenates them.
    """
    return "".join(list(map(
        lambda x: pool[ secrets.randbelow( len(pool) ) ],
        list(range(size))
        )))

def create_keys(
    length: int,
    amount: int,
    pool: List[chr] = POOL
    ) -> List[str]:
    """(x: int, y: int) -> List[str]
    return x passwords with y length.
    """
    return [create_key(length, pool) for _ in range(amount)]
