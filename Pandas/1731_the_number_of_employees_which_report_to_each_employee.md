# [The Number of Employees Which Report to Each Employee](https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/description/)

Table: Employees
```
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| reports_to  | int      |
| age         | int      |
+-------------+----------+
employee_id is the column with unique values for this table.
This table contains information about the employees and the id of the manager they report to. Some employees do not report to anyone (reports_to is null). 
``` 

For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them.

Write a solution to report the ids and the names of all managers, the number of employees who report directly to them, and the average age of the reports rounded to the nearest integer.

Return the result table ordered by employee_id.

The result format is in the following example.

Example 1:
```
Input: 
Employees table:
+-------------+---------+------------+-----+
| employee_id | name    | reports_to | age |
+-------------+---------+------------+-----+
| 9           | Hercy   | null       | 43  |
| 6           | Alice   | 9          | 41  |
| 4           | Bob     | 9          | 36  |
| 2           | Winston | null       | 37  |
+-------------+---------+------------+-----+
Output: 
+-------------+-------+---------------+-------------+
| employee_id | name  | reports_count | average_age |
+-------------+-------+---------------+-------------+
| 9           | Hercy | 2             | 39          |
+-------------+-------+---------------+-------------+
Explanation: Hercy has 2 people report directly to him, Alice and Bob. Their average age is (41+36)/2 = 38.5, which is 39 after rounding it to the nearest integer.
```
Solution
```python
import pandas as pd
import numpy as np


def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
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
```