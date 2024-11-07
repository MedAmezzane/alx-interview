#!/usr/bin/python3
"""
N Queens Solver

This module provides a solution to the N Queens problem, which involves
placing N queens on an N x N chessboard so that no two queens threaten
each other.
"""

import sys

# Validate command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Ensure that the argument is a positive integer
if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

# Ensure that N is at least 4
n = int(sys.argv[1])
if n < 4:
    print("N must be at least 4")
    sys.exit(1)


def queens(n, row=0, columns=[], diag1=[], diag2=[]):
    """
    Recursively finds all valid configurations of queens on the board.

    Args:
        n (int): The size of the chessboard (N x N).
        row (int): The current row being processed.
        columns (list): Tracks columns where queens are placed.
        diag1 (list): Tracks left-to-right diagonals where queens are placed.
        diag2 (list): Tracks right-to-left diagonals where queens are placed.

    Yields:
        list: A list representing a valid configuration of queen placements.
    """
    if row < n:
        for col in range(n):
            if col not in columns and row + col not in diag1 and row - col not in diag2:
                yield from queens(n, row + 1, columns + [col], diag1 + [row + col], diag2 + [row - col])
    else:
        yield columns


def solve(n):
    """
    Solves the N Queens problem and prints each solution as a list of
    coordinates.

    Args:
        n (int): The size of the chessboard (N x N).
    """
    result = []  # Holds the coordinates for the current solution
    row_index = 0  # Tracks the current row index for printing

    for solution in queens(n):
        for col in solution:
            result.append([row_index, col])
            row_index += 1
        print(result)
        result = []
        row_index = 0


# Run the N Queens solver
solve(n)
