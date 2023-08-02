def tictactoe(moves):
    matrix = [[0 for _ in range(3)] for _ in range(3)]
    winner = None

    for i, (x, y) in enumerate(moves):
        matrix[x][y] = 1 if i % 2 == 0 else 5

    def check_winner(arr):
        nonlocal winner
        if sum(arr) == 3:
            winner = 'A'
        if sum(arr) == 15:
            winner = 'B'

    for row in matrix:
        check_winner(row)

    for col in zip(*matrix):
        check_winner(col)

    dig1 = [matrix[0][0], matrix[1][1], matrix[2][2]]
    dig2 = [matrix[0][2], matrix[1][1], matrix[2][0]]
    check_winner(dig1)
    check_winner(dig2)

    return winner or ('Draw' if len(moves) == 9 else 'Pending')


print(tictactoe(moves=[[0, 0], [2, 0], [1, 1], [2, 1], [2, 2]]))
