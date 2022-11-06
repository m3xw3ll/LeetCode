# [Set Matrix Zeroes](https://leetcode.com/problems/set-matrix-zeroes/)

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:

![](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)

```
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
```
Example 2:

![](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)

```
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
```
Solution
```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return []

        rowl = len(matrix)
        coll = len(matrix[0])
        first_cell_row_zero = False
        first_cell_col_zero = False

        for row in range(rowl):
            for col in range(coll):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_cell_row_zero = True
                    if col == 0:
                        first_cell_col_zero = True
                    matrix[row][0] = matrix[0][col] = 0

        for row in range(1, rowl):
            for col in range(1, coll):
                matrix[row][col] = 0 if matrix[0][col] == 0 or matrix[row][0] == 0 else matrix[row][col]

        if first_cell_row_zero:
            for col in range(coll):
                matrix[0][col] = 0

        if first_cell_col_zero:
            for row in range(rowl):
                matrix[row][0] = 0
```