#[Number of Valid Clock Times](https://leetcode.com/problems/number-of-valid-clock-times/description/)

You are given a string of length 5 called time, representing the current time on a digital clock in the format "hh:mm". 
The earliest possible time is "00:00" and the latest possible time is "23:59".

In the string time, the digits represented by the ? symbol are unknown, and must be replaced with a digit from 0 to 9.

Return an integer answer, the number of valid clock times that can be created by replacing every ? with a digit from 0 
to 9.

Example 1:
```
Input: time = "?5:00"
Output: 2
Explanation: We can replace the ? with either a 0 or 1, producing "05:00" or "15:00". Note that we cannot replace it with a 2, since the time "25:00" is invalid. In total, we have two choices.
```
Example 2:
```
Input: time = "0?:0?"
Output: 100
Explanation: Each ? can be replaced by any digit from 0 to 9, so we have 100 total choices.
```
Example 3:
```
Input: time = "??:??"
Output: 1440
Explanation: There are 24 possible choices for the hours, and 60 possible choices for the minutes. In total, we have 24 * 60 = 1440 choices.
```
Solution
```python
class Solution:
    def countTime(self, time: str) -> int:
        h1, h2, _, m1, m2 = time
        out = 1
        if h1 == '?' and h2 == '?':
            out *= 24
        elif h1 == '?':
            if int(h2) >= 4:
                out *= 2
            else:
                out *= 3
        elif h2 == '?':
            if int(h1) <= 1:
                out *= 10
            else:
                out *= 4

        if m1 == '?' and m2 == '?':
            out *= 60
        elif m1 == '?':
            out *= 6
        elif m2 == '?':
            out *= 10

        return out
```