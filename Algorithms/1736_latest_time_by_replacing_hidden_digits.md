# [Latest Time by Replacing Hidden Digits](https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/description/)

You are given a string time in the form of  hh:mm, where some of the digits in the string are hidden (represented by ?).

The valid times are those inclusively between 00:00 and 23:59.

Return the latest valid time you can get from time by replacing the hidden digits.

Example 1:
```
Input: time = "2?:?0"
Output: "23:50"
Explanation: The latest hour beginning with the digit '2' is 23 and the latest minute ending with the digit '0' is 50.
```
Example 2:
```
Input: time = "0?:3?"
Output: "09:39"
```
Example 3:
```
Input: time = "1?:22"
Output: "19:22"
```
Solution
```python
class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        for idx, char in enumerate(time):
            if char == '?':
                if idx == 0:
                    time[idx] = '2' if time[1] <= '3' or time[1] == '?' else '1'
                elif idx == 1:
                    time[idx] = '3' if time[0] == '2' else '9'
                elif idx == 3:
                    time[idx] = '5'
                elif idx == 4:
                    time[idx] = '9'
        return ''.join(time)
```