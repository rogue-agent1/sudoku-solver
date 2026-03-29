#!/usr/bin/env python3
"""Sudoku Solver - Solve puzzles using constraint propagation and backtracking."""
import sys

def solve(board):
    empty = find_empty(board)
    if not empty: return True
    r, c = empty
    for n in range(1, 10):
        if valid(board, r, c, n):
            board[r][c] = n
            if solve(board): return True
            board[r][c] = 0
    return False

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0: return (r, c)
    return None

def valid(board, r, c, n):
    if n in board[r]: return False
    if n in [board[i][c] for i in range(9)]: return False
    br, bc = 3*(r//3), 3*(c//3)
    for i in range(br, br+3):
        for j in range(bc, bc+3):
            if board[i][j] == n: return False
    return True

def display(board):
    for i, row in enumerate(board):
        if i % 3 == 0 and i: print("  ------+-------+------")
        line = ""
        for j, v in enumerate(row):
            if j % 3 == 0 and j: line += " | "
            line += f" {v if v else '.'}"
        print(f"  {line}")

def parse(s):
    board = []
    digits = [c for c in s if c in "0123456789."]
    for i in range(9):
        row = []
        for j in range(9):
            c = digits[i*9+j] if i*9+j < len(digits) else "0"
            row.append(0 if c == "." else int(c))
        board.append(row)
    return board

def main():
    puzzle = "530070000600195000098000060800060003400803001700020006060000280000419005000080079"
    if len(sys.argv) > 1: puzzle = sys.argv[1]
    board = parse(puzzle)
    print("=== Sudoku Solver ===\n\nPuzzle:"); display(board)
    if solve(board): print("\nSolution:"); display(board)
    else: print("\nNo solution exists.")

if __name__ == "__main__":
    main()
