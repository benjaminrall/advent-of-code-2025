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
TEST_RESULT = 25272

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        points = [list(map(int, line.strip().split(','))) for line in f.readlines()]

    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distances.append((math.hypot(points[i][0] - points[j][0], points[i][1] - points[j][1], points[i][2] - points[j][2]), i, j))
    distances.sort()

    circuits = [-1 for _ in range(len(points))]
    lengths = []
    for i in range(len(distances)):
        _, a, b = distances[i]
        if circuits[a] < 0 and circuits[b] < 0:
            # Both disconnected: form new circuit of length 2
            circuits[a] = len(lengths)
            circuits[b] = len(lengths)
            lengths.append(2)
        elif circuits[a] < 0 or circuits[b] < 0:
            # One disconnected: join new node to existing circuit
            circuit = max(circuits[a], circuits[b])
            circuits[a] = circuit
            circuits[b] = circuit
            lengths[circuit] += 1
        elif circuits[a] != circuits[b]:
            # Both connected, but to different circuits: join circuits
            lengths[circuits[a]] += lengths[circuits[b]]
            lengths[circuits[b]] = -1
            circuits = [c if c != circuits[b] else circuits[a] for c in circuits]
        if lengths[circuits[a]] == len(points):            
            return points[a][0] * points[b][0]

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
