# [Employee Bonus](https://leetcode.com/problems/employee-bonus/description/?lang=pythondata)

Table: Employee
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| empId       | int     |
| name        | varchar |
| supervisor  | int     |
| salary      | int     |
+-------------+---------+
empId is the column with unique values for this table.
Each row of this table indicates the name and the ID of an employee in addition to their salary and the id of their manager.
```
Table: Bonus
```
+-------------+------+
| Column Name | Type |
+-------------+------+
| empId       | int  |
| bonus       | int  |
+-------------+------+
empId is the column of unique values for this table.
empId is a foreign key (reference column) to empId from the Employee table.
Each row of this table contains the id of an employee and their respective bonus.
``` 

Write a solution to report the name and bonus amount of each employee with a bonus less than 1000.

Return the result table in any order.

The result format is in the following example.

Example 1:
```
Input: 
Employee table:
+-------+--------+------------+--------+
| empId | name   | supervisor | salary |
+-------+--------+------------+--------+
| 3     | Brad   | null       | 4000   |
| 1     | John   | 3          | 1000   |
| 2     | Dan    | 3          | 2000   |
| 4     | Thomas | 3          | 4000   |
+-------+--------+------------+--------+
Bonus table:
+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
Output: 
+------+-------+
| name | bonus |
+------+-------+
| Brad | null  |
| John | null  |
| Dan  | 500   |
+------+-------+
```
Solution
```python
import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
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
```