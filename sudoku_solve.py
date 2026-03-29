import argparse, sys

def parse_grid(text):
    grid = []
    for c in text:
        if c.isdigit(): grid.append(int(c))
        elif c == ".": grid.append(0)
    return [grid[i*9:(i+1)*9] for i in range(9)]

def valid(grid, r, c, n):
    if n in grid[r]: return False
    if n in [grid[i][c] for i in range(9)]: return False
    br, bc = 3*(r//3), 3*(c//3)
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            if grid[i][j] == n: return False
    return True

def solve(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for n in range(1, 10):
                    if valid(grid, r, c, n):
                        grid[r][c] = n
                        if solve(grid): return True
                        grid[r][c] = 0
                return False
    return True

def display(grid):
    for i, row in enumerate(grid):
        if i % 3 == 0 and i > 0: print("------+-------+------")
        line = ""
        for j, v in enumerate(row):
            if j % 3 == 0 and j > 0: line += "| "
            line += f"{v if v else '.'} "
        print(line)

def main():
    p = argparse.ArgumentParser(description="Sudoku solver")
    p.add_argument("puzzle", nargs="?", help="81-char string (0 or . for empty)")
    p.add_argument("--demo", action="store_true")
    args = p.parse_args()
    if args.demo:
        puzzle = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
    elif args.puzzle:
        puzzle = args.puzzle
    else:
        puzzle = sys.stdin.read().strip()
    grid = parse_grid(puzzle)
    print("Puzzle:")
    display(grid)
    if solve(grid):
        print("\nSolution:")
        display(grid)
    else:
        print("No solution exists")

if __name__ == "__main__":
    main()
