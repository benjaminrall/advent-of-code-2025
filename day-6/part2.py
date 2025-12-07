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
TEST_RESULT = 3263827

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip('\n') for line in f.readlines()]

    ops = lines[-1].split()
    lines = lines[:-1]

    ns = []
    op_ns = []
    for col in zip(*lines):
        if all([x == ' ' for x in col]):
            ns.append(op_ns)
            op_ns = []
        else :
            op_ns.append(int(''.join(col)))
    if op_ns:
        ns.append(op_ns)

    total = 0
    for op, ns in zip(ops, ns):
        initial = 1 if op == '*' else 0
        fold = (lambda x, y : x * y) if op == '*' else (lambda x, y : x + y)
        for n in ns:
            initial = fold(initial, n)
        total += initial

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
