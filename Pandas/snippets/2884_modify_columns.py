import pandas as pd


def modify_salary_column(data):
    data['salary'] = data['salary'].apply(lambda x: x * 2)
    return data


if __name__ == '__main__':
    data = [['Jack', 19666], ['Piper', 74754], ['Mia', 62509], ['Ulysses', 54866]]
    employees = pd.DataFrame(data, columns=['name', 'salary'])
    print(modify_salary_column(employees))