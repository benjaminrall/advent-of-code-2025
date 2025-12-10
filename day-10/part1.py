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
TEST_RESULT = 7

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip().split() for line in f.readlines()]
    
    total = 0
    for line in lines:
        target, buttons = line[0], line[1:-1]
        target = np.array([0 if c == '.' else 1 for c in target[1:-1]])
        buttons = [np.array(list(map(int, button[1:-1].split(',')))) for button in buttons]
        lights = np.zeros_like(target)

        def search(i, lights, selected):
            if all(lights == target):
                return selected
            if i >= len(buttons):
                return np.inf
                        
            new_lights = lights.copy()
            new_lights[buttons[i]] = (lights[buttons[i]] + 1) % 2
            return min(
                search(i + 1, new_lights, selected + 1),
                search(i + 1, lights, selected)
            )
        
        total += search(0, lights, 0)

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
