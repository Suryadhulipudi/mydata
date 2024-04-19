import random

def is_valid(board, row, col, num):
    # Check if the number is already present in the current row
    if num in board[row]:
        return False
    
    # Check if the number is already present in the current column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check if the number is already present in the current 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def solve_sudoku(board):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    
    row, col = empty_cell
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None

def generate_sudoku_board():
    board = [[0 for _ in range(9)] for _ in range(9)]
    solve_sudoku(board)
    return board

def print_board(board):
    for row in board:
        print(row)

# Generate a Sudoku board
sudoku_board = generate_sudoku_board()

# Print the generated Sudoku board
print("Generated Sudoku Board:")
print_board(sudoku_board)
