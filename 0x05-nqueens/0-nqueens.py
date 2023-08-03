import sys

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def is_valid(board, row, col):
    # Check if there is a queen in the same column
    for i in range(len(board)):
        if board[i][col] == 'Q':
            return False
    
    # Check diagonals
    for i, j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 'Q':
            return False
    for i, j in zip(range(row,len(board)), range(col,-1,-1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_nqueens(n):
    board = [['.'] * n for _ in range(n)]

    def backtrack(row):
        if row == n:
            print_board(board)
            return
        
        for col in range(n):
            if is_valid(board, row, col):
                board[row][col] = 'Q'
                backtrack(row+1)
                board[row][col] = '.'

    backtrack(0)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    n = 0  
    try:
        n = int(sys.argv[1])  
    except:
        print("N must be a number")
        sys.exit(1)
    
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)
