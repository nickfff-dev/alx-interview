#!/usr/bin/python3
"""N-Queens problem using backtracking."""

import sys


def print_usage():
    """Print usage message and exit."""
    print("Usage: nqueens N")
    sys.exit(1)


def is_number(s):
    """Check if the given string is a number."""
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col, n):
    """Solve the N Queens problem."""
    if col >= n:
        # All queens are placed
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        print(solution)
        return

    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            solve_n_queens(board, col + 1, n)

            # If placing queen in board[i][col] doesn't lead to a solution,
            # remove it
            board[i][col] = 0


def main():
    """Main function."""
    if len(sys.argv) != 2:
        print_usage()

    n = sys.argv[1]
    if not is_number(n):
        print("N must be a number")
        sys.exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Solve the N Queens problem
    solve_n_queens(board, 0, n)


if __name__ == "__main__":
    main()
