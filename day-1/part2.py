# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = 1
YEAR = 2025

# The expected result from the test input, if using a test input
TEST_RESULT = 6

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    total = 0
    dial = 50
    for line in lines:
        direction, value = line[0], int(line[1:])
        inc = 1 if direction == 'R' else -1
        for _ in range(value):
            dial = (dial + inc) % 100
            if dial == 0:
                total += 1

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
