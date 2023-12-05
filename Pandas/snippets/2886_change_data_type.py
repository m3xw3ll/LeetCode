import pandas as pd


def change_data_type(students):
    students['grade'] = students['grade'].astype(int)
    return students


if __name__ == '__main__':
    data = [[1, 'Ava', 6, 73.0], [2, 'Kate', 15, 87.0]]
    students = pd.DataFrame(data, columns=['student_id', 'name', 'age', 'grade']).astype(
        {'student_id': 'int', 'name': 'object', 'age': 'int', 'grade': 'float'})
    print(change_data_type(students))