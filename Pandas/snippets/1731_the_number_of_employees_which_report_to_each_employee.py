import pandas as pd
import numpy as np


def count_employees(employees):
    data = employees.groupby('reports_to').agg(reports_count=('reports_to','count'),average_age=('age', 'mean')).reset_index()
    out = employees.merge(data, left_on='employee_id', right_on='reports_to')
    out = out[['employee_id', 'name', 'reports_count', 'average_age']]
    out['average_age'] = np.where(out['average_age'] - np.floor(out['average_age']) < 0.5,
                             np.floor(out['average_age']),
                             np.ceil(out['average_age']))
    return out.sort_values(by='employee_id')


if __name__ == '__main__':
    data = [[9, 'Hercy', None, 43], [6, 'Alice', 9, 41], [4, 'Bob', 9, 36], [2, 'Winston', None, 37]]
    employees = pd.DataFrame(data, columns=['employee_id', 'name', 'reports_to', 'age']).astype(
        {'employee_id': 'Int64', 'name': 'object', 'reports_to': 'Int64', 'age': 'Int64'})
    print(count_employees(employees))