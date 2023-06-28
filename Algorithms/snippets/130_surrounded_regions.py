def solve(board):
    rows = len(board)
    cols = len(board[0])

    def dfs(i, j):
        if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != 'O':
            return
        board[i][j] = '#'
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O' and (r in [0, rows - 1] or c in [0, cols - 1]):
                dfs(r, c)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'O':
                board[r][c] = 'X'

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == '#':
                board[r][c] = 'O'

    return board


print(solve(board=[["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]))
