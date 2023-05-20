def sort_the_students(score, k):
    return sorted(score, key=lambda row: row[k], reverse=True)


print(sort_the_students(score=[[10, 6, 9., 1], [7, 5, 11, 2], [4, 8, 3, 15]], k=2))
