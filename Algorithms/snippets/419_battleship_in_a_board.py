def count_battleships(board):
    rows = len(board)
    cols = len(board[0])
    cnt = 0
    path = set()

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in path:
            return
        path.add((r, c))
        if board[r][c] == 'X':
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'X' and (r, c) not in path:
                dfs(r, c)
                cnt += 1
    return cnt


print(count_battleships(board=[["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]))
