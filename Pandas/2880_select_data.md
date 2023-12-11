# [Select Data](https://leetcode.com/problems/select-data/description/)

DataFrame students
```
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+
```
Write a solution to select the name and age of the student with student_id = 101.

The result format is in the following example.

Example 1:
```
Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
Output:
+---------+-----+
| name    | age | 
+---------+-----+
| Ulysses | 13  |
+---------+-----+
Explanation:
Student Ulysses has student_id = 101, we select the name and age.
```
Solution
```python
import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    tmp = students.loc[students['student_id'] == 101]
    return tmp[['name', 'age']]


if __name__ == '__main__':
    data = [[101, 'Ulysses', 13],
            [53, 'William', 10],
            [128, 'Henry', 6],
            [3, 'Henry', 11]]

    students = pd.DataFrame(data, columns=['student_id', 'name', 'age'])
    print(selectData(students))
```