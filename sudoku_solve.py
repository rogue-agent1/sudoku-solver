#!/usr/bin/env python3
"""sudoku_solve - Backtracking sudoku solver."""
import sys, argparse, json

def parse_grid(s):
    s = s.replace(".", "0").replace(" ", "").replace(",", "")
    nums = [int(c) for c in s if c.isdigit()]
    return [nums[i:i+9] for i in range(0, 81, 9)]

def is_valid(grid, row, col, num):
    if num in grid[row]: return False
    if num in [grid[r][col] for r in range(9)]: return False
    br, bc = 3*(row//3), 3*(col//3)
    for r in range(br, br+3):
        for c in range(bc, bc+3):
            if grid[r][c] == num: return False
    return True

def solve(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for num in range(1, 10):
                    if is_valid(grid, r, c, num):
                        grid[r][c] = num
                        if solve(grid): return True
                        grid[r][c] = 0
                return False
    return True

def render(grid):
    lines = []
    for i, row in enumerate(grid):
        if i % 3 == 0 and i > 0: lines.append("------+-------+------")
        parts = []
        for j in range(0, 9, 3):
            parts.append(" ".join(str(c) if c else "." for c in row[j:j+3]))
        lines.append(" | ".join(parts))
    return "
".join(lines)

def main():
    p = argparse.ArgumentParser(description="Sudoku solver")
    p.add_argument("puzzle", help="81-digit string (0 or . for empty)")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    grid = parse_grid(args.puzzle)
    given = sum(1 for r in grid for c in r if c > 0)
    solved = solve(grid)
    if args.json:
        print(json.dumps({"solved": solved, "given": given, "grid": grid}))
    else:
        if solved: print(render(grid))
        else: print("No solution found")

if __name__ == "__main__": main()
