from typing import Dict
from functools import lru_cache

memo: Dict[int, int] = {0: 0, 1: 1}


def fib(n: int) -> int:
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    if n < 2:
        return n
    return memo[n]


@lru_cache(maxsize=None)
def fib_lru(n: int) -> int:
    if n < 2:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)


def fib_iter(n: int) -> int:
    if n < 2:
        return n
    last_n: int = 0
    next_n: int = 1

    for _ in range(1, n):
        last_n, next_n = next_n, last_n + next_n
    return next_n


if __name__ == "__main__":
    print(fib_lru(499))     #recursive max at 499
    print(fib_iter(1000))   #iterative performing better and handling more
