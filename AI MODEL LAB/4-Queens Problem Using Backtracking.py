
N = 4

board = [-1] * N
solutions = []

def is_safe(row, col):
    for i in range(row):
        if board[i] == col:
            return False

        if abs(board[i] - col) == abs(i - row):
            return False

    return True

def solve(row):
    if row == N:
        solutions.append(board.copy())
        return

    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            solve(row + 1)
            board[row] = -1

# Solve the problem
solve(0)

# Display all solutions
print("Total Solutions:", len(solutions))

for solution in solutions:
    for row in range(N):
        for col in range(N):
            if solution[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
    print()
