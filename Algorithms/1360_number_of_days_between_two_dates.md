# [Number of Days Between Two Dates](https://leetcode.com/problems/number-of-days-between-two-dates/)

Write a program to count the number of days between two dates.

The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Example 1:
```
Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1
```
Example 2:
```
Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
```
Solution
```python
import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = datetime.datetime.strptime(date1, '%Y-%m-%d')
        date2 = datetime.datetime.strptime(date2, '%Y-%m-%d')

        return abs((date2 - date1).days)
```