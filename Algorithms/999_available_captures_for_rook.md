# [Available Captures for Rook](https://leetcode.com/problems/available-captures-for-rook/description/)

On an 8 x 8 chessboard, there is exactly one white rook 'R' and some number of white bishops 'B', black pawns 'p', and 
empty squares '.'.

When the rook moves, it chooses one of four cardinal directions (north, east, south, or west), then moves in that 
direction until it chooses to stop, reaches the edge of the board, captures a black pawn, or is blocked by a white 
bishop. A rook is considered attacking a pawn if the rook can capture the pawn on the rook's turn. The number of 
available captures for the white rook is the number of pawns that the rook is attacking.

Return the number of available captures for the white rook.

Example 1:

![](https://assets.leetcode.com/uploads/2019/02/20/1253_example_1_improved.PNG)

```
Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: In this example, the rook is attacking all the pawns.
```
Example 2:

![](https://assets.leetcode.com/uploads/2019/02/19/1253_example_2_improved.PNG)

```
Input: board = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 0
Explanation: The bishops are blocking the rook from attacking any of the pawns.
```
Example 3:

![](https://assets.leetcode.com/uploads/2019/02/20/1253_example_3_improved.PNG)

```
Input: board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
Output: 3
Explanation: The rook is attacking the pawns at positions b5, d6, and f5.
```
Solution
```python
class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    rx, ry = i, j

        out = 0
        for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            x, y = rx + i, ry + j
            while 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] == 'p':
                    out += 1
                if board[x][y] != '.':
                    break
                x += i
                y += j
        return out
```