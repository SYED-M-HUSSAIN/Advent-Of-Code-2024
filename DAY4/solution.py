# Read the content of the file
with open('/workspaces/Advent-Of-Code-2024/DAY4/input.txt', 'r') as file:
    # Split the file into lines and create a list of lists
    matrix = [list(line.strip()) for line in file]


def check_forward(row, y):
    """Check for the pattern 'XMAS' in forward direction."""
    if row[y:y+4] == ['X', 'M', 'A', 'S']:
        print("forward")
        return 1
    return 0

def check_backward(row, y):
    """Check for the pattern 'XMAS' in backward direction."""
    if row[y:y+4] == ['S', 'A', 'M', 'X']:
        print("backward")
        return 1
    return 0

def check_vertical(matrix, cp, y):
    """Check for the pattern 'XMAS' in the vertical direction."""
    if cp + 3 < len(matrix):
        # Up-down check
        if [matrix[cp+i][y] for i in range(4)] == ['X', 'M', 'A', 'S']:
            print("updown")
            return 1
        # Down-up check
        if [matrix[cp+i][y] for i in range(4)] == ['S', 'A', 'M', 'X']:
            print("updown")
            return 1
    return 0

def check_diagonal(matrix, cp, y):
    """Check for the pattern 'XMAS' in the diagonal direction."""
    if cp + 3 < len(matrix) and y + 3 < len(matrix[cp]):
        # Top-left to bottom-right
        if [matrix[cp+i][y+i] for i in range(4)] == ['X', 'M', 'A', 'S']:
            print("diagonal")
            return 2
        # Bottom-right to top-left
        if [matrix[cp+i][y+i] for i in range(4)] == ['S', 'A', 'M', 'X']:
            print("diagonal")
            return 2
    return 0

def count_xmas_patterns(matrix):
    """Count all instances of the pattern 'XMAS' in various directions."""
    count = 0
    for cp, row in enumerate(matrix):
        for y in range(len(row)):
            if (len(row) - y) > 3:
                count += check_forward(row, y)
            if y >= 3:
                count += check_backward(row, y - 3)
            count += check_vertical(matrix, cp, y)
            if (len(row) - y) > 3:
                count += check_diagonal(matrix, cp, y)
        print("END", cp)
    print(count)
    print(len(matrix))
    return count


answer=(count_xmas_patterns(matrix))
print(f"Number of XMAS patterns: {answer}")


## PART 2
def count_x_mas_patterns(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    # Helper function to check if a pattern is "MAS" or "SAM"
    def is_mas_or_sam(cells):
        return cells == ["M", "A", "S"] or cells == ["S", "A", "M"]

    # Iterate through each cell as the center
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] == "A":
                # Check diagonals for X-MAS patterns
                # Top-left to bottom-right
                if (
                    r > 0 and r < rows - 1 and c > 0 and c < cols - 1
                    and is_mas_or_sam([grid[r - 1][c - 1], grid[r][c], grid[r + 1][c + 1]])
                    and is_mas_or_sam([grid[r - 1][c + 1], grid[r][c], grid[r + 1][c - 1]])
                ):
                    count += 1

    return count


# Calculate the result
result = count_x_mas_patterns(matrix)
print(f"Number of X-MAS patterns: {result}")
