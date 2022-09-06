# [Search Insert Position](https://leetcode.com/problems/search-insert-position/)

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return 
the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
```
Input: nums = [1,3,5,6], target = 5
Output: 2
```
Example 2:
```
Input: nums = [1,3,5,6], target = 2
Output: 1
```
Example 3:
```
Input: nums = [1,3,5,6], target = 7
Output: 4
```
Solution
```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            if target < nums[middle]:
                right = middle -1
            else:
                left = middle + 1

        return left
```
