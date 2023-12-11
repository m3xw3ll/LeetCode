import pandas as pd


def select_data(students):
    tmp = students.loc[students['student_id'] == 101]
    return tmp[['name', 'age']]


if __name__ == '__main__':
    data = [[101, 'Ulysses', 13],
            [53, 'William', 10],
            [128, 'Henry', 6],
            [3, 'Henry', 11]]

    students = pd.DataFrame(data, columns=['student_id', 'name', 'age'])
    print(select_data(students))