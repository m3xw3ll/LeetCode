import pandas as pd


def create_bonus_column(employee):
    employees['bonus'] = employee['salary'] * 2
    return employees


if __name__ == '__main__':
    data = [['Piper', 4548],
            ['Grace', 28150],
            ['Georgia', 1103],
            ['Willow', 6593],
            ['Finn', 74576],
            ['Thomas', 24433],]
    employees = pd.DataFrame(data, columns=['name', 'salary'])
    print(create_bonus_column(employees))