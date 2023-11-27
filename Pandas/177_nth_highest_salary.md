# [Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/description/?envType=list&envId=e8vku1ke)

Table: Employee
```
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.
```

Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

The result format is in the following example.

Example 1:
```
Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+
```
Example 2:
```
Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
Output: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
```
Solution
```python
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
```