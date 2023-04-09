# [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/description/)

You are given an m x n integer matrix matrix with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.
- Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:

![](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
```
Example 2:

![](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)

```
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
```
Solution
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_matrix = [item for sublist in matrix for item in sublist]
        left = 0
        right = len(flat_matrix) - 1

        while left <= right:
            middle = (left + right) // 2
            if flat_matrix[middle] == target:
                return True
            elif flat_matrix[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return False
```
