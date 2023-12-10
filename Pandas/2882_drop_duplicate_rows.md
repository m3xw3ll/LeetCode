# [Drop Duplicate Rows](https://leetcode.com/problems/drop-duplicate-rows/description/)

DataFrame customers
```
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| customer_id | int    |
| name        | object |
| email       | object |
+-------------+--------+
```
There are some duplicate rows in the DataFrame based on the email column.

Write a solution to remove these duplicate rows and keep only the first occurrence.

The result format is in the following example.

Example 1:
```
Input:
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 5           | Finn    | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
Output:  
+-------------+---------+---------------------+
| customer_id | name    | email               |
+-------------+---------+---------------------+
| 1           | Ella    | emily@example.com   |
| 2           | David   | michael@example.com |
| 3           | Zachary | sarah@example.com   |
| 4           | Alice   | john@example.com    |
| 6           | Violet  | alice@example.com   |
+-------------+---------+---------------------+
Explanation:
Alic (customer_id = 4) and Finn (customer_id = 5) both use john@example.com, so only the first occurrence of this email is retained.
```
Solution
```python
import pandas as pd


def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset='email', keep='first')


if __name__ == '__main__':
    data = [[1, 'Ella', 'emily@example.com'],
            [2, 'David', 'michael@example.com'],
            [3, 'Zachary', 'sarah@example.com'],
            [4, 'Alice', 'john@example.com'],
            [5, 'Finn', 'john@example.com'],
            [6, 'Violet', 'alice@example.com']]
    customers = pd.DataFrame(data, columns=['customer_id', 'name', 'email'])
    print(dropDuplicateEmails(customers))
```