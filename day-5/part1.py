# Placeholders to be filled when copying the template
PART = 1
DAY = 5
YEAR = 2025

# The expected result from the test input, if using a test input
TEST_RESULT = 3

def merge_ranges(range1, range2):
    a, b = range1
    c, d = range2
    if c > b:
        return False, (a, b)
    return True, (a, max(b, d))

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    ranges = []

    s = lines.index('')
    ranges = []
    for line in lines[:s]:
        a, b = map(int, line.split('-'))
        ranges.append((a, b))
    ranges.sort()

    complete_ranges = []
    current = ranges[0]
    for i in range(1, len(ranges)):
        merged, current = merge_ranges(current, ranges[i])
        if not merged:
            complete_ranges.append(current)
            current = ranges[i]
    complete_ranges.append(current)

    total = 0
    for line in lines[s+1:]:
        for a, b in complete_ranges:
            if a <= int(line) <= b:
                total += 1
                break

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
