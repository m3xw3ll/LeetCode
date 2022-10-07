# [Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)

Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of 
negative numbers in grid.

Example 1:
```
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.
```
Example 2:
```
Input: grid = [[3,2],[1,0]]
Output: 0
```
Solution
```python
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum(self.binary_search(row) for row in grid)
    
    def binary_search(self, row):
        left = 0
        right = len(row) - 1

        while left <= right:
            middle = (left + right) // 2
            if row[middle] < 0:
                right = middle - 1
            else:
                left = middle + 1
        return len(row) - left
```