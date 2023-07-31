# [Range Addition II](https://leetcode.com/problems/range-addition-ii/description/)

You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] 
means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.

Example 1:

![](https://assets.leetcode.com/uploads/2020/10/02/ex1.jpg)

```
Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
```
Example 2:
```
Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
Output: 4
```
Example 3:
```
Input: m = 3, n = 3, ops = []
Output: 9
```
Solution
```python
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row = m
        min_col = n
        for x, y in ops:
            min_row = min(x, min_row)
            min_col = min(y, min_col)
        return min_row * min_col
```