# [Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/)

Table: Employee
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
```

Write a solution to find managers with at least five direct reports.

Return the result table in any order.

The result format is in the following example.

Example 1:
```
Input: 
Employee table:
+-----+-------+------------+-----------+
| id  | name  | department | managerId |
+-----+-------+------------+-----------+
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
+-----+-------+------------+-----------+
Output: 
+------+
| name |
+------+
| John |
+------+
```
Solution
```python
import pandas as pd


def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
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
```
