# Placeholders to be filled when copying the template
PART = 1
DAY = 4
YEAR = 2025

# The expected result from the test input, if using a test input
TEST_RESULT = 13

def get_neighbours(grid, pos):
    total = 0 
    for i in range(pos[0]-1, pos[0]+2):
        if i < 0 or i >= len(grid):
            continue
        for j in range(pos[1]-1, pos[1]+2):
            if j < 0 or j >= len(grid[0]):
                continue
            if i == pos[0] and j == pos[1]:
                continue
            total += grid[i][j]
    return total
    

# Method to solve the input stored in a given file name
def solve(filename: str) -> int:
    # --- SOLUTION CODE ---
    with open(filename) as f:
        grid = [[1 if c =='@' else 0 for c in line.strip()] for line in f.readlines()]
    
    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] and get_neighbours(grid, (r,c)) < 4:
                total += 1

    return total

if __name__ == "__main__":
    print(f"Test solution: {solve('test.txt')}")
    print(f"Actual solution: {solve('input.txt')}")
