#!/usr/bin/python3
"""
Module to solve the N-Queens problem.
The program outputs all possible solutions for placing N queens
on an N x N chessboard such that no two queens threaten each other.
"""

import sys

if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        # Handle non-integer input
        print("N must be a number")
        sys.exit(1)

    # Ensure N meets the minimum required board size for a valid solution
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
