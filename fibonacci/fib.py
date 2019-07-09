# dumb fib implementation with recursion
def fib_recur(n: int) -> int:
    if n < 2:
        return n
    return fib_recur(n - 1) + fib_recur(n - 2)

# fib implementation with dictionary memoization
from typing import Dict

memo_table: Dict[int, int] = {0: 0, 1: 1}
def fib_memo(n: int) -> int:
    if n not in memo_table:
        memo_table[n] = fib_memo(n - 1) + fib_memo(n - 2)
    return memo_table[n]

# fib implementation with auto lru cache
from functools import lru_cache
@lru_cache()
def fib_lru(n: int) -> int:
    if n < 2:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)

# fib implementation with iterator
def fib_iter(n: int) -> int:
    if n < 2:
        return n
    last_n: int = 0
    next_n: int = 1
    for _ in range(1, n):
        last_n, next_n = next_n, last_n + next_n
    return next_n
#fib iterator with a generator
from typing import Generator
def fib_generator(n: int) -> Generator[int, None, None]:
    yield 0 #first item in fib
    if n > 0:
        yield 1 #second item in fib
    last_n: int = 0
    next_n: int = 1

    for _ in range(1, n):
        last_n, next_n = next_n, last_n + next_n
        yield next_n
    

if __name__ == "__main__":
    print(fib_recur(10))
    print(fib_memo(10))
    print(fib_memo(100))
    print(fib_lru(100))
    print(fib_iter(100))
    print(fib_iter(1000))
    for i in fib_generator(50):
        print(i)