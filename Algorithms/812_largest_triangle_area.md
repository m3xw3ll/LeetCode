# [Largest Triangle Area](https://leetcode.com/problems/largest-triangle-area/)

Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle 
that can be formed by any three different points. Answers within 10-5 of the actual answer will be accepted.

Example 1:

![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/04/04/1027.png)

Example 1:
```
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000
Explanation: The five points are shown in the above figure. The red triangle is the largest.
```
Example 2:
```
Input: points = [[1,0],[0,0],[0,1]]
Output: 0.50000
```
Solution
```python
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        out = 0
        l = len(points)

        for i in range(l):
            x1, y1 = points[i]
            for j in range(i+1, l):
                x2, y2 = points[j]
                for k in range(j+1, l):
                    x3, y3 = points[k]
                    out = max(out, abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))))
        return out
```
