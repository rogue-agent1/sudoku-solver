#!/usr/bin/env python3
"""sudoku_solve - Solve sudoku puzzles using backtracking."""
import sys

def parse(s):
    nums = [int(c) if c.isdigit() else 0 for c in s if c.isdigit() or c in '.0']
    return [nums[i:i+9] for i in range(0,81,9)]

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
        if i % 3 == 0 and i: print('  ------+-------+------')
        line = '  '
        for j, v in enumerate(row):
            if j % 3 == 0 and j: line += '| '
            line += f'{v} ' if v else '. '
        print(line)

def main():
    args = sys.argv[1:]
    if not args or '-h' in args:
        print("Usage: sudoku_solve.py PUZZLE_STRING\n  (81 chars, 0 or . for empty)"); return
    puzzle = args[0] if len(args[0]) >= 81 else open(args[0]).read().replace('\n','')
    grid = parse(puzzle)
    print("Input:"); display(grid); print()
    if solve(grid): print("Solved:"); display(grid)
    else: print("No solution")

if __name__ == '__main__': main()
