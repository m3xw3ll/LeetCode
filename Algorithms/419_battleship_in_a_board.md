# [Battleship in a Board](https://leetcode.com/problems/battleships-in-a-board/description/)

Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on 
board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 
1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical 
cell separates between two battleships (i.e., there are no adjacent battleships).

Example 1:

![](https://assets.leetcode.com/uploads/2021/04/10/battelship-grid.jpg)

```
Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
```
Example 2:
```
Input: board = [["."]]
Output: 0
```
Solution
```python
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        cols = len(board[0])
        cnt = 0
        path = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in path:
                return
            path.add((r, c))
            if board[r][c] == 'X':
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X' and (r, c) not in path:
                    dfs(r, c)
                    cnt += 1
        return cnt
```
