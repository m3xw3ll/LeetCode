import pandas as pd


def create_dataframe(student):
    return pd.DataFrame(student, columns=['student_id', 'age'])


if __name__ == '__main__':
    student_data = [[1,15],[2,11],[3,11],[4,20]]
    print(create_dataframe(student_data))