# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 2
YEAR = 2025

# The expected result from the test input, if using a test input
TEST_RESULT = 1227775554

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    ranges = [list(map(int, r.split('-'))) for r in lines[0].split(',')]

    total = 0
    for r in ranges:
        for i in range(r[0], r[1] + 1):
            s = str(i)
            if len(s) % 2 == 1:
                continue
            if s[:len(s) // 2] == s[len(s) // 2:]:
                total += i

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
