# [Valid Boomerang](https://leetcode.com/problems/valid-boomerang/)

Given an array points where points[i] = [xi, yi] represents a point on the X-Y plane, return true if these points are 
a boomerang.

A boomerang is a set of three points that are all distinct and not in a straight line.

Example 1:
```
Input: points = [[1,1],[2,3],[3,2]]
Output: true
```
Example 2:
```
Input: points = [[1,1],[2,2],[3,3]]
Output: false
```
Solution
```python
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, x2, x3 = points[0][0], points[1][0], points[2][0]
        y1, y2, y3 = points[0][1], points[1][1], points[2][1]

        a = (x1 * (y2 - y3) +
             x2 * (y3 - y1) +
             x3 * (y1 - y2))

        return False if a == 0 else True
```

