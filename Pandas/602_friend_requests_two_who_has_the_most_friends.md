# [Friend Requests II: Who Has the Most Friends](https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/description/)

Table: RequestAccepted
```
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
(requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
This table contains the ID of the user who sent the request, the ID of the user who received the request, and the date when the request was accepted.
``` 

Write a solution to find the people who have the most friends and the most friends number.

The test cases are generated so that only one person has the most friends.

The result format is in the following example.

Example 1:
```
Input: 
RequestAccepted table:
+--------------+-------------+-------------+
| requester_id | accepter_id | accept_date |
+--------------+-------------+-------------+
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
+--------------+-------------+-------------+
Output: 
+----+-----+
| id | num |
+----+-----+
| 3  | 3   |
+----+-----+
Explanation: 
The person with id 3 is a friend of people 1, 2, and 4, so he has three friends in total, which is the most number than any others.
```
Solution
```python
import pandas as pd
from collections import Counter


def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    lst = request_accepted['requester_id'].values.tolist() + request_accepted['accepter_id'].values.tolist()
    most_common = Counter(lst).most_common(1)
    out = pd.DataFrame([[most_common[0][0], most_common[0][1]]], columns=['id', 'num'])
    return out


if __name__ == '__main__':
    data = [[1, 2, '2016/06/03'], [1, 3, '2016/06/08'], [2, 3, '2016/06/08'], [3, 4, '2016/06/09']]
    request_accepted = pd.DataFrame(data, columns=['requester_id', 'accepter_id', 'accept_date']).astype(
        {'requester_id': 'Int64', 'accepter_id': 'Int64', 'accept_date': 'datetime64[ns]'})
    print(most_friends(request_accepted))
```