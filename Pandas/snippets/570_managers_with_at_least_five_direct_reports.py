import pandas as pd


def find_managers(employee):
    tmp = employee.groupby(['managerId'])['id'].count().reset_index(name='count')
    tmp = tmp[tmp['count'] >= 5]
    out = pd.merge(employee, tmp, left_on='id', right_on='managerId', how='inner')
    return out[['name']]


if __name__ == '__main__':
    data = [[101, 'John', 'A', None], [102, 'Dan', 'A', 101], [103, 'James', 'A', 101], [104, 'Amy', 'A', 101],
            [105, 'Anne', 'A', 101], [106, 'Ron', 'B', 101]]
    employee = pd.DataFrame(data, columns=['id', 'name', 'department', 'managerId']).astype(
        {'id': 'Int64', 'name': 'object', 'department': 'object', 'managerId': 'Int64'})
    print(find_managers(employee))