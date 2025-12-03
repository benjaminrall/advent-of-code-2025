# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 1
DAY = 3
YEAR = 2025

# The expected result from the test input, if using a test input
TEST_RESULT = 357

@cache
def find_batteries(bank: str, length: int):
    if length == 0 or len(bank) == 0:
        return 0

    if length == len(bank):
        return int(bank)

    return max(
        int(bank[0]) * 10 ** (length - 1) + find_batteries(bank[1:], length - 1), 
        find_batteries(bank[1:], length)
    )

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    return sum([find_batteries(bank, 2) for bank in lines])

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
