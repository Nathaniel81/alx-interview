#!/usr/bin/python3
"""
Module: 0-nqueens.py
"""
import sys


def is_valid(board, row, col):
    """Checks if the position of queen is valid"""
    # Check this row on left side
    if 1 in board[row]:
        return False

    upper_diag = zip(range(row, -1, -1),
                     range(col, -1, -1))
    for i, j in upper_diag:
        if board[i][j] == 1:
            return False

    lower_diag = zip(range(row, len(board), 1),
                     range(col, -1, -1))
    for i, j in lower_diag:
        if board[i][j] == 1:
            return False

    return True


def nqueens_helper(board, col):
    """Helper method"""
    if col >= len(board):
        print_board(board, len(board))
    for i in range(len(board)):
        if is_valid(board, i, col):
            board[i][col] = 1
            result = nqueens_helper(board, col + 1)
            if result:
                return True
            board[i][col] = 0
    return False


def print_board(board, n):
    """Prints the position of the queen on board"""
    b = []

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                b.append([i, j])
    print(b)


def nqueens(n):
    """Intrance function for the puzzle"""
    board = []
    for i in range(n):
        row = [0] * n
        board.append(row)
    nqueens_helper(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    queens = sys.argv[1]
    if not queens.isnumeric():
        print("N must be a number")
        exit(1)
    elif int(queens) < 4:
        print("N must be at least 4")
        exit(1)
    nqueens(int(queens))
