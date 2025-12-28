# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
from graphlib import TopologicalSorter

# Placeholders to be filled when copying the template
PART = 1
DAY = None
YEAR = None

# The expected result from the test input, if using a test input
TEST_RESULT = 5

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
    graph = defaultdict(set)
    for line in lines:
        a, b = line.split(': ')
        b = b.split()
        for x in b:
            graph[a].add(x)

    ts = TopologicalSorter(graph)
    ordered = list(ts.static_order())
    you_i = ordered.index('you')
    out_i = ordered.index('out')
    if out_i < you_i:
        ordered = list(reversed(ordered))
        you_i = ordered.index('you')
        out_i = ordered.index('out')

    counts = defaultdict(int)
    counts['you'] = 1
    for i in range(you_i, out_i):
        node = ordered[i]
        for child in graph[node]:
            counts[child] += counts[node]

    return counts['out']

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
