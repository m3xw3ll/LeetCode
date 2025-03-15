# [Consecutive Numbers](https://leetcode.com/problems/consecutive-numbers/description/)

Table: Logs
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column.
``` 

Find all numbers that appear at least three times consecutively.

Return the result table in any order.

The result format is in the following example.

Example 1:
```
Input: 
Logs table:
+----+-----+
| id | num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
Output: 
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
Explanation: 1 is the only number that appears consecutively for at least three times.
```
Solution
```python
import pandas as pd


def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['tmp'] = logs['num'].rolling(window=3).var()
    nums = logs[logs['tmp'] == 0]['num'].unique().tolist()
    return pd.DataFrame(nums, columns=['ConsecutiveNums'])


if __name__ == '__main__':
    data = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
    logs = pd.DataFrame(data, columns=['id', 'num']).astype({'id': 'Int64', 'num': 'Int64'})
    print(consecutive_numbers(logs))
```