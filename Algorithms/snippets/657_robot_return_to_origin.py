def judge_circle(moves):
    return moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D')


print(judge_circle('UD'))