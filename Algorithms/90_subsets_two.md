# [Subsets II](https://leetcode.com/problems/subsets-ii/description/)

Given an integer array nums that may contain duplicates, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
```
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
```
Example 2:
```
Input: nums = [0]
Output: [[],[0]]
```
Solution
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = set()
        nums = sorted(nums)

        def bt(i, curr):
            out.add(curr)
            for i in range(i, len(nums)):
                bt(i + 1, tuple(list(curr) + [nums[i]]))

        bt(0, tuple())
        return out
```