# [Permutations](https://leetcode.com/problems/permutations/)

Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
```
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
```
Example 2:
```
Input: nums = [0,1]
Output: [[0,1],[1,0]]
```
Example 3:
```
Input: nums = [1]
Output: [[1]]
```
Solution
```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        l = []
        for i in range(len(nums)):
            m = nums[i]
            rem = nums[:i] + nums[i+1:]

            for p in self.permute(rem):
                l.append([m] + p)
        return l
```