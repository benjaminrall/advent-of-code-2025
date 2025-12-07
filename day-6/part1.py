# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = None
YEAR = None

# The expected result from the test input, if using a test input
TEST_RESULT = 4277556

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip().split() for line in f.readlines()]

    total = 0
    for x in zip(*lines):
        ns = x[:-1]
        op = x[-1]
        initial = 1 if op == '*' else 0
        fold = (lambda x, y : x * y) if op == '*' else (lambda x, y : x + y)
        for n in ns:
            initial = fold(initial, int(n))
        total += initial

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
