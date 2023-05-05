# [Count Lattice Points Inside a Circle](https://leetcode.com/problems/count-lattice-points-inside-a-circle/description/)

Given a 2D integer array circles where circles[i] = [xi, yi, ri] represents the center (xi, yi) and radius ri of the ith
circle drawn on a grid, return the number of lattice points that are present inside at least one circle.

Note:

- A lattice point is a point with integer coordinates.
- Points that lie on the circumference of a circle are also considered to be inside it.

Example 1:

![](https://assets.leetcode.com/uploads/2022/03/02/exa-11.png)

```
Input: circles = [[2,2,1]]
Output: 5
Explanation:
The figure above shows the given circle.
The lattice points present inside the circle are (1, 2), (2, 1), (2, 2), (2, 3), and (3, 2) and are shown in green.
Other points such as (1, 1) and (1, 3), which are shown in red, are not considered inside the circle.
Hence, the number of lattice points present inside at least one circle is 5.
```
Example 2:

![](https://assets.leetcode.com/uploads/2022/03/02/exa-22.png)

```
Input: circles = [[2,2,2],[3,4,1]]
Output: 16
Explanation:
The figure above shows the given circles.
There are exactly 16 lattice points which are present inside at least one circle. 
Some of them are (0, 2), (2, 0), (2, 4), (3, 2), and (4, 4).
```
Solution
```python
class Solution:
    def is_point_in_circle(self, x, y, r, square_x, square_y):
        return ((square_x - x) ** 2 + (square_y - y) ** 2) <= r * r

    def countLatticePoints(self, circles: List[List[int]]) -> int:
        points = set()
        for cx, cy, cr in circles:
            for px in range(cx - cr, cx + cr + 1):
                for py in range(cy - cr, cy + cr + 1):
                    if (px, py) not in points and self.is_point_in_circle(cx, cy, cr, px, py):
                        points.add((px, py))
        return len(points)
```