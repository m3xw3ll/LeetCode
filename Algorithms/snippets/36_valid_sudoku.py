def is_valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    square = [[set() for _ in range(3)] for _ in range(3)]

    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == '.':
                continue
            if val in rows[i] or val in cols[j] or val in square[i//3][j//3]:
                return False
            rows[i].add(val)
            cols[j].add(val)
            square[i//3][j//3].add(val)
    return True



print(is_valid_sudoku(board=
                      [["5", "3", ".", ".", "7", ".", ".", ".", "."]
                          , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                          , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                          , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                          , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                          , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                          , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                          , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                          , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
