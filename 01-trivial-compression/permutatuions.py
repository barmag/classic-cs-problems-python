from itertools import permutations

s = "ABCDE"

count = 0
if __name__ == "__main__":
    for p in permutations(s):
        count += 1
        print(f"perm {count}: {p}")