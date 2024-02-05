import pandas as pd


def top_three_salaries(employee, department):
    salaries = employee[['departmentId', 'salary']].drop_duplicates()
    top_three = salaries.sort_values(by='salary', ascending=False).groupby('departmentId').head(3)
    top_three = pd.merge(top_three, department, left_on='departmentId', right_on='id').rename(columns={'name': 'Department'})
    out = pd.merge(top_three, employee, left_on=['salary', 'id'], right_on=['salary', 'departmentId'])
    return out[['Department', 'name', 'salary']].rename(columns={'name': 'Employee', 'salary': 'Salary'})


if __name__ == '__main__':
    data = [[1, 'Joe', 85000, 1], [2, 'Henry', 80000, 2], [3, 'Sam', 60000, 2], [4, 'Max', 90000, 1],
            [5, 'Janet', 69000, 1], [6, 'Randy', 85000, 1], [7, 'Will', 70000, 1]]
    employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype(
        {'id': 'Int64', 'name': 'object', 'salary': 'Int64', 'departmentId': 'Int64'})
    data = [[1, 'IT'], [2, 'Sales']]
    department = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    print(top_three_salaries(employee, department))