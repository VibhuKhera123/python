def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens_util(board, row, N):
    if row == N:
        # All queens have been placed, print the solution
        for i in range(N):
            for j in range(N):
                print(board[i][j], end=" ")
            print()
        print()
        return True

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_n_queens_util(board, row + 1, N)
            board[row][col] = 0

    return False

def solve_n_queens(N):
    board = [[0] * N for _ in range(N)]
    solve_n_queens_util(board, 0, N)

# Test the program
N = int(input("Enter the number of queens: "))
solve_n_queens(N)