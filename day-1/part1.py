# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 1
YEAR = 2025

# The expected result from the test input, if using a test input
TEST_RESULT = 3

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    total = 0
    dial = 50
    for line in lines:
        direction, value = line[0], int(line[1:])
        if direction == 'L':
            value *= -1
        dial = (dial + value) % 100
        if dial == 0:
            total += 1

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
