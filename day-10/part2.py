# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
from itertools import combinations
from scipy.optimize import milp, LinearConstraint, Bounds

# Placeholders to be filled when copying the template
PART = 2
DAY = None
YEAR = None

# The expected result from the test input, if using a test input
TEST_RESULT = 33

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip().split() for line in f.readlines()]
    
    total = 0
    for i, line in enumerate(lines):
        target, buttons = line[-1], line[1:-1]
        target = np.array([int(n) for n in target[1:-1].split(',')])
        buttons = [np.array(list(map(int, button[1:-1].split(',')))) for button in buttons]

        M = np.zeros(shape=(len(target), len(buttons)))
        for i, button in enumerate(buttons):
            M[button, i] = 1

        c = np.ones(len(buttons))
        constraints = LinearConstraint(M, target, target)
        integrality = np.ones(len(buttons))
        bounds = Bounds(lb=0, ub=np.inf)

        res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)
        total += int(sum(res.x))

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
