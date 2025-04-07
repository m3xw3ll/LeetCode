# [Check if Two Chessboard Squares Have the Same Color](https://leetcode.com/problems/check-if-two-chessboard-squares-have-the-same-color/description/)

You are given two strings, coordinate1 and coordinate2, representing the coordinates of a square on an 8 x 8 chessboard.

Below is the chessboard for reference.

![](https://assets.leetcode.com/uploads/2024/07/17/screenshot-2021-02-20-at-22159-pm.png)

Return true if these two squares have the same color and false otherwise.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first (indicating its column), and the number second (indicating its row).

Example 1:
```
Input: coordinate1 = "a1", coordinate2 = "c3"

Output: true

Explanation:

Both squares are black.
```
Example 2:
```
Input: coordinate1 = "a1", coordinate2 = "h3"

Output: false

Explanation:

Square "a1" is black and "h3" is white.
```
Solution
```python
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        c1_sum = int(ord(coordinate1[0].lower()) - ord('a') + 1) + int(coordinate1[1])
        c2_sum = int(ord(coordinate2[0].lower()) - ord('a') + 1) + int(coordinate2[1])
        return c1_sum % 2 == c2_sum % 2
```

