# [Circle and Rectangle Overlapping](https://leetcode.com/problems/circle-and-rectangle-overlapping/description/)

You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented as 
(x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the 
top-right corner of the rectangle.

Return true if the circle and rectangle are overlapped otherwise return false. In other words, check if there is any 
point (xi, yi) that belongs to the circle and the rectangle at the same time.

Example 1:

![](https://assets.leetcode.com/uploads/2020/02/20/sample_4_1728.png)

```
Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0).
```
Example 2:
```
Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false
```
Example 3:

![](https://assets.leetcode.com/uploads/2020/02/20/sample_2_1728.png)

```
Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
Output: true
```
Solution
```python
class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        nearest_x = max(x1, min(x2, xCenter))
        nearest_y = max(y1, min(y2, yCenter))
        dist_x = nearest_x - xCenter
        dist_y = nearest_y - yCenter

        return dist_x ** 2 + dist_y ** 2 <= radius ** 2
```