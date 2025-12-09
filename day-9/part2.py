# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
from itertools import combinations

# Placeholders to be filled when copying the template
PART = 2
DAY = None
YEAR = None

# The expected result from the test input, if using a test input
TEST_RESULT = 24

def calculate_area(point1, point2):
    y0, x0 = point1
    y1, x1 = point2
    return (abs(y1 - y0) + 1) * (abs(x1 - x0) + 1)

def get_rect(p1, p2):
    return (np.minimum(p1, p2), np.maximum(p1, p2))

def is_contained(rect, edges):
    p1, p2 = rect
    for e1, e2 in edges:
        if p1[0] < e2[0] and p1[1] < e2[1] and p2[0] > e1[0] and p2[1] > e1[1]:
            return False
    return True

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        points = [np.array(list(map(int, line.strip().split(',')))) for line in f.readlines()]
    rects = sorted(combinations(points, 2), key=lambda pair : calculate_area(*pair))
    edges = [get_rect(p1, p2) for p1, p2 in zip(points, points[1:] + points[:1])]
    
    for p1, p2 in reversed(rects):
        rect = get_rect(p1, p2)
        if is_contained(rect, edges):
            return calculate_area(*rect)

    return 0

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
