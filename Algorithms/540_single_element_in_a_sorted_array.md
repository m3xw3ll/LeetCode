# [Single Element in a Sorted Array](https://leetcode.com/problems/single-element-in-a-sorted-array/description/)

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one 
element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:
```
Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
```
Example 2:
```
Input: nums = [3,3,7,7,10,11,11]
Output: 10
```
Solution
```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle = (left + right) // 2
            if middle % 2 == 1:
                middle -= 1
            if nums[middle] != nums[middle + 1]:
                right = middle
            else:
                left = middle + 2
        return nums[left]
```