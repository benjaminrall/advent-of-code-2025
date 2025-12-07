# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict

# Placeholders to be filled when copying the template
PART = 2
DAY = None
YEAR = None

# The expected result from the test input, if using a test input
TEST_RESULT = 40



# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    splitters = []
    for line in lines[1:]:
        s = set([j for j in range(len(line)) if line[j] == '^'])
        if s:
            splitters.append(s)
    @cache
    def search(beam, depth):
        if depth >= len(splitters):
            return 1
        
        if beam in splitters[depth]:
            return search(beam - 1, depth + 1) + search(beam + 1, depth + 1)
        else:
            return search(beam, depth + 1)

    return search(lines[0].index('S'), 0)

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
