def count_students(students, sandwiches):
    while len(students) != 0:
        if sandwiches[0] not in students:
            return len(students)
        elif sandwiches[0] == students[0]:
            students.pop(0)
            sandwiches.pop(0)
        else:
            tmp = students.pop(0)
            students.append(tmp)
    return len(students)


print(count_students(students=[1, 1, 0, 0], sandwiches=[0, 1, 0, 1]))
