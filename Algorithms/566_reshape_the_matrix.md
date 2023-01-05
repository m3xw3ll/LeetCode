# [Reshape The Matrix](https://leetcode.com/problems/reshape-the-matrix/description/)

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different 
size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of 
the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as 
they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output 
the original matrix.

Example 1:

![](https://assets.leetcode.com/uploads/2021/04/24/reshape1-grid.jpg)

```
Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
```

![](https://assets.leetcode.com/uploads/2021/04/24/reshape2-grid.jpg)

```
Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]
```
Solution
```python
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = []
        out = []

        for row in mat:
            for num in row:
                flat.append(num)

        if len(flat) != r * c:
            return mat

        for i in range(r):
            out.append(flat[i*c:i*c+c])
        return out
```