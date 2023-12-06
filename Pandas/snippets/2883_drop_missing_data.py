import pandas as pd


def drop_missing_data(students):
    return students.dropna(subset=['name'])


if __name__ == '__main__':
    data = [[32, 'Piper', 5],
            [217, None, 19],
            [779, 'Georgia', 20],
            [849, 'Willow', 14]]
    students = pd.DataFrame(data, columns=['student_id', 'name', 'age'])
    print(drop_missing_data(students))