def is_valid(row, col, board):
    for i in range(row):
        if board[i] == col or \
            board[i] - i == col - row or \
            board[i] + i == col + row:
            return False
    return True

def solve(size, row, board, results):
    if row == size:
        results.append(board[:])
        return
    for col in range(size):
        if is_valid(row, col, board):
            board[row] = col
            solve(size, row + 1, board, results)
            board[row] -= 1


def find_all_solutions(size):
    results = []
    board = [-1] * size
    solve(size, 0, board, results)
    return results

i = 0
n = 8
all_solutions = find_all_solutions(n)
for solution in all_solutions:
    i+=1

print(f"Для {n} ферзей: {i} решений")
