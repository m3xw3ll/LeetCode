import math


def divide_players(skill):
    skill = sorted(skill)
    out = 0
    left = 0
    right = len(skill) - 1
    team_score = skill[left] + skill[right]
    while left < right:
        tmp_score = skill[left] + skill[right]
        if tmp_score != team_score: return -1
        out += skill[left] * skill[right]
        left += 1
        right -= 1
    return out


print(divide_players([1, 1, 2, 3]))
