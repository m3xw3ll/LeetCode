def number_of_employees_who_met_target(hours, target):
    return len([i for i in hours if i >= target])


print(number_of_employees_who_met_target(hours=[0, 1, 2, 3, 4], target=2))
