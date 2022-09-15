# [Day of the Year](https://leetcode.com/problems/day-of-the-year/)

Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

Example 1:
```
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
```
Example 2:
```
Input: date = "2019-02-10"
Output: 41
```
Solution
```python
class Solution:
    def is_leap(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    def dayOfYear(self, date: str) -> int:
        date = date.split('-')
        days_dict = {
            0: 31,
            1: 28,
            2: 31,
            3: 30,
            4: 31,
            5: 30,
            6: 31,
            7: 31,
            8: 30,
            9: 31,
            10: 30,
            11: 31
        }

        if self.is_leap(int(date[0])):
            days_dict[1] = 29
        out = 0
        for i in range(0, int(date[1])-1):
            out += days_dict[i]

        return out + int(date[2])
```