# [Sort an Array](https://leetcode.com/problems/sort-an-array/)

Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest 
space complexity possible.

Example 1:
```
Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the 
positions of other numbers are changed (for example, 1 and 5).
```
Example 2:
```
Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
```
Solution
```python
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            r = len(nums)//2
            L = nums[:r]
            M = nums[r:]

            self.sortArray(L)
            self.sortArray(M)

            i = j = k = 0

            while i < len(L) and j < len(M):
                if L[i] < M[j]:
                    nums[k] = L[i]
                    i += 1
                else:
                    nums[k] = M[j]
                    j += 1
                k += 1
            while i < len(L):
                nums[k] = L[i]
                i += 1
                k += 1

            while j < len(M):
                nums[k] = M[j]
                j += 1
                k += 1
        return nums
```