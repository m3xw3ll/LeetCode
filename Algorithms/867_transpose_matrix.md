# [Transpose Matrix](https://leetcode.com/problems/transpose-matrix/)

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

![](https://assets.leetcode.com/uploads/2021/02/10/hint_transpose.png)

Example 1:
```
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
```
Example 2:
```
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
```
Solution
```python
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        out = []
        for c in range(len(matrix[0])):
            out.append([0] * len(matrix))

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                out[j][i] = matrix[i][j]
        return out
```