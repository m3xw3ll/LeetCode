# [Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/)

Given an m x n matrix, return true if the matrix is Toeplitz. Otherwise, return false.

A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same elements.

Example 1:

![](https://assets.leetcode.com/uploads/2020/11/04/ex1.jpg)

```
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: true
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
```
Example 2:

![](https://assets.leetcode.com/uploads/2020/11/04/ex2.jpg)

```
Input: matrix = [[1,2],[2,2]]
Output: false
Explanation:
The diagonal "[1, 2]" has different elements.
```
Solution:
```python
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] != matrix[r-1][c-1]:
                    return False
        return True
```