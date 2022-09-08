# [Find Peak Element](https://leetcode.com/problems/find-peak-element/)

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks,
return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater 
than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:
```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```
Example 2:
```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the 
peak element is 6.
```
Solution
```python
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if len(nums) == 1:
            return 0
        if nums[-1] > nums[-2]:
            return right

        while left <= right:
            middle = (left + right) // 2
            if (nums[middle] > nums[middle-1]) and (nums[middle] > nums[middle+1]):
                return middle
            if nums[middle-1] > nums[middle]:
                right = middle -1
            else:
                left = middle +1
        return -1
```