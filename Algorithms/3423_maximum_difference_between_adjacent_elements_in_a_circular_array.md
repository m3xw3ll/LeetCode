# [Maximum Difference Between Adjacent Elements in a Circular Array](https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description/)

Given a circular array nums, find the maximum absolute difference between adjacent elements.

Note: In a circular array, the first and last elements are adjacent.

Example 1:
```
Input: nums = [1,2,4]

Output: 3

Explanation:

Because nums is circular, nums[0] and nums[2] are adjacent. They have the maximum absolute difference of |4 - 1| = 3.
```
Example 2:
```
Input: nums = [-5,-10,-5]

Output: 5

Explanation:

The adjacent elements nums[0] and nums[1] have the maximum absolute difference of |-5 - (-10)| = 5.
```
Solution
```python
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        edgecase = abs(nums[0] - nums[len(nums) - 1])
        ret = 0
        for i in range(0, len(nums) - 1):
            ret = max(ret, abs(nums[i] - nums[i+1]))
        return max(ret, edgecase)
```