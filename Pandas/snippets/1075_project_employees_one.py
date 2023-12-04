import pandas as pd


def project_employees_i(project, employee):
    data = pd.merge(project, employee, how='inner', left_on='employee_id', right_on='employee_id')
    data = (data.groupby(['project_id'])['experience_years'].mean().round(2).reset_index()
            .rename(columns={'experience_years': 'average_years'}))
    return data


if __name__ == '__main__':
    data = [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]]
    project = pd.DataFrame(data, columns=['project_id', 'employee_id']).astype(
        {'project_id': 'Int64', 'employee_id': 'Int64'})
    data = [[1, 'Khaled', 3], [2, 'Ali', 2], [3, 'John', 1], [4, 'Doe', 2]]
    employee = pd.DataFrame(data, columns=['employee_id', 'name', 'experience_years']).astype(
        {'employee_id': 'Int64', 'name': 'object', 'experience_years': 'Int64'})
    print(project_employees_i(project=project, employee=employee))
