def average(salary):
    salary = sorted(salary)
    return sum(salary[1:-1]) / (len(salary) - 2)


print(average([4000, 3000, 1000, 2000]))
