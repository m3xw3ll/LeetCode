import pandas as pd


def rename_columns(students):
    return students.rename(columns={'id': 'student_id',
                                    'first': 'first_name',
                                    'last': 'last_name',
                                    'age': 'age_in_years'})


if __name__ == '__main__':
    data = [[1, 'Mason', 'King', 6],
            [2, 'Ava', 'Wright', 7],
            [3, 'Taylor', 'Hall', 16],
            [4, 'Georgia', 'Thompson', 18],
            [5, 'Thomas', 'Moore', 10]]
    students = pd.DataFrame(data, columns=['id', 'first', 'last', 'age'])
    print(rename_columns(students))