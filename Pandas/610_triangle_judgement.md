# [Triangle Judgement](https://leetcode.com/problems/triangle-judgement/description/)

Table: Triangle
```
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.
``` 

Report for every three line segments whether they can form a triangle.

Return the result table in any order.

The result format is in the following example.

Example 1:
```
Input: 
Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+
Output: 
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+
```
Solution
```python
import pandas as pd


def check_sides(row):
    sorted_row = sorted(row)
    smallest = sorted_row[0]
    second_smallest = sorted_row[1]
    third_smallest = sorted_row[2]
    return "Yes" if smallest + second_smallest > third_smallest else "No"


def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle['triangle'] = triangle.apply(check_sides, axis=1)
    return triangle


if __name__ == '__main__':
    data = [[13, 15, 30], [10, 20, 15]]
    triangle = pd.DataFrame(data, columns=['x', 'y', 'z']).astype({'x': 'Int64', 'y': 'Int64', 'z': 'Int64'})
    print(triangle_judgement(triangle))
```