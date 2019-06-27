from typing import Dict
from functools import lru_cache

memo: Dict[int, int] = {0: 0, 1: 1}
def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n-1) + fib(n-2)
    if n < 2:
        return n
    return memo[n]

@lru_cache(maxsize=5)
def fib_lru(n: int) -> int:
    if n < 2:
        return n
    return fib_lru(n-1) + fib_lru(n-2)

if __name__ == "__main__":
    print(fib_lru(200))