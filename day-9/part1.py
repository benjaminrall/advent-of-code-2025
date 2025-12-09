# Useful imports
import math
import numpy as np
from functools import cache
from collections import defaultdict
from itertools import combinations

# Placeholders to be filled when copying the template
PART = 1
DAY = None
YEAR = None

# The expected result from the test input, if using a test input
TEST_RESULT = 50

def calculate_area(point1, point2):
    y0, x0 = point1
    y1, x1 = point2
    return (abs(y1 - y0) + 1) * (abs(x1 - x0) + 1)

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        points = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]
    rects = sorted(combinations(points, 2), key=lambda pair : calculate_area(*pair))
    return calculate_area(*rects[-1])

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
