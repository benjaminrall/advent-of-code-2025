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
TEST_RESULT = 21

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    beams = set([lines[0].index('S')])
    splitters = []
    for line in lines[1:]:
        s = [j for j in range(len(line)) if line[j] == '^']
        if s:
            splitters.append(s)

    splits = 0
    for splitter in splitters:
        new_beams = beams
        for x in splitter:
            if x in beams:
                new_beams.remove(x)
                new_beams.add(x - 1)
                new_beams.add(x + 1)
                splits += 1
        beams = new_beams
    
    return splits

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
