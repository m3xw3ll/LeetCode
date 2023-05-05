# [Maximum Number of Fish in a Grid](https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/)

You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:

- A land cell if grid[r][c] = 0, or
- A water cell containing grid[r][c] fish, if grid[r][c] > 0.

A fisher can start at any water cell (r, c) and can do the following operations any number of times:

- Catch all the fish at cell (r, c), or
- Move to any adjacent water cell.

Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.

An adjacent cell of the cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) or (r - 1, c) if it exists.

Example 1:

![](https://assets.leetcode.com/uploads/2023/03/29/example.png)

```
Input: grid = [[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4 fish.
```
Example 2:

![](https://assets.leetcode.com/uploads/2023/03/29/example2.png)

```
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
Output: 1
Explanation: The fisher can start at cells (0,0) or (3,3) and collect a single fish. 
```
Solution
```python
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visit = [[False] * cols for r in range(rows)]
        out = 0

        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0 or visit[i][j]:
                return 0
            visit[i][j] = True
            return dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1) + grid[i][j]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] and not visit[i][j]:
                    out = max(out, dfs(i, j))
        return out
```