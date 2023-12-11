import pandas as pd


def concatenate_tables(df1, df2):
    return pd.concat([df1, df2])


if __name__  == '__main__':
    data1 = [[1, 'Mason', 8],
             [2, 'Ava', 6],
             [3, 'Taylor', 15],
             [4, 'Georgia', 17]]

    data2 = [[5, 'Leo', 7],
             [6, 'Alex', 7]]

    df1 = pd.DataFrame(data1, columns=['student_id', 'name', 'age'])
    df2 = pd.DataFrame(data2, columns=['student_id', 'name', 'age'])
    print(concatenate_tables(df1, df2))