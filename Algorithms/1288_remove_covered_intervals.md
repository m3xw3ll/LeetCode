# [Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/description/)

Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are 
covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

Example 1:
```
Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
```
Example 2:
```
Input: intervals = [[1,4],[2,3]]
Output: 1
```
Solution
```python
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))
        out = 0
        end = 0
        for _, e in intervals:
            if e > end:
                out += 1
                end = e
        return out
```