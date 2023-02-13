# [Surface Area of 3D Shapes](https://leetcode.com/problems/surface-area-of-3d-shapes/description/)

You are given an n x n grid where you have placed some 1 x 1 x 1 cubes. Each value v = grid[i][j] represents a tower 
of v cubes placed on top of cell (i, j).

After placing these cubes, you have decided to glue any directly adjacent cubes to each other, forming several 
irregular 3D shapes.

Return the total surface area of the resulting shapes.

Note: The bottom face of each shape counts toward its surface area.

Example 1:

![](https://assets.leetcode.com/uploads/2021/01/08/tmp-grid2.jpg)

```
Input: grid = [[1,2],[3,4]]
Output: 34
```
Example 2:

![](https://assets.leetcode.com/uploads/2021/01/08/tmp-grid4.jpg)

```
Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 32
```
Example 3:

![](https://assets.leetcode.com/uploads/2021/01/08/tmp-grid5.jpg)

```
Input: grid = [[2,2,2],[2,1,2],[2,2,2]]
Output: 46
```
Solution
```python
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        out = 0
        n = len(grid)

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    out += (grid[i][j] * 4) + 2
                if i:
                    out -= min(grid[i][j], grid[i - 1][j]) * 2
                if j:
                    out -= min(grid[i][j], grid[i][j - 1]) * 2
        return out
```