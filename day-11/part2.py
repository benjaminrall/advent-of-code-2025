# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
from graphlib import TopologicalSorter

# Placeholders to be filled when copying the template
PART = 2
DAY = None
YEAR = None

# The expected result from the test input, if using a test input
TEST_RESULT = 2

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
    start = ordered.index('svr')
    end = ordered.index('out')
    if end < start:
        ordered = list(reversed(ordered))
        start = ordered.index('svr')
        end = ordered.index('out')
    midpoint_a = ordered.index('fft')
    midpoint_b = ordered.index('dac')
    if midpoint_b < midpoint_a:
        midpoint_a, midpoint_b = midpoint_b, midpoint_a

    def path(start, end):
        counts = defaultdict(int)
        counts[ordered[start]] = 1
        for i in range(start, end):
            node = ordered[i]
            for child in graph[node]:
                counts[child] += counts[node]
        return counts[ordered[end]]

    return path(start, midpoint_a) * path(midpoint_a, midpoint_b) * path(midpoint_b, end)

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
