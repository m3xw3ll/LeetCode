import pandas as pd


def employee_bonus(employee, bonus):
    data = pd.merge(employee, bonus, on='empId', how='left')
    data = data[['name', 'bonus']]
    return data[(data['bonus'] < 1000) | data['bonus'].isna()]


if __name__ == '__main__':
    data = [[3, 'Brad', None, 4000], [1, 'John', 3, 1000], [2, 'Dan', 3, 2000], [4, 'Thomas', 3, 4000]]
    employee = pd.DataFrame(data, columns=['empId', 'name', 'supervisor', 'salary']).astype(
        {'empId': 'Int64', 'name': 'object', 'supervisor': 'Int64', 'salary': 'Int64'})
    data = [[2, 500], [4, 2000]]
    bonus = pd.DataFrame(data, columns=['empId', 'bonus']).astype({'empId': 'Int64', 'bonus': 'Int64'})
    print(employee_bonus(employee=employee, bonus=bonus))