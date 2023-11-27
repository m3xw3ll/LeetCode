import pandas as pd


def n_th_highest_salary(employee, N):
    employee['Salary'].drop_duplicates()
    employee = employee.sort_values(by=['Salary'], ascending=False)
    if len(employee) < N:
        return pd.DataFrame([None], columns=[f'getMthHighestSalary({N})'])
    else:
        return pd.DataFrame([employee['Salary'][N-1]], columns=[f'getMthHighestSalary({N})'])


if __name__ == '__main__':
    data = [[1, 100], [2, 200], [3, 300]]
    employee = pd.DataFrame(data, columns=['Id', 'Salary']).astype({'Id': 'Int64', 'Salary': 'Int64'})
    print(n_th_highest_salary(employee, 2))