#!/usr/bin/python3
"""
N-Queens problem solver using backtracking.
"""


import sys


def nqueens_helper(n, y, board):
    """
    Helper function for N-Queens backtracking.
    """
    for i in range(n):
        held = 0
        for j in board:
            # Check if the queen can be placed in the current position
            if i == j[1] or abs(i - j[1]) == abs(y - j[0]):
                held = 1
                break
        if held == 0:
            board.append([y, i])
            if y == n - 1:
                # If the last row is reached, print the solution
                print(board)
            else:
                # Continue placing queens in the next row
                nqueens_helper(n, y + 1, board)
            board.pop()  # Backtrack: remove the last queen placement


def nqueens(n):
    """
    Solve the N-Queens problem for a chessboard of size n x n.
    """
    board = []
    nqueens_helper(n, 0, board)


def main():
    """
    Main function to handle command-line input and call N-Queens solver.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    nqueens(n)


if __name__ == "__main__":
    main()
