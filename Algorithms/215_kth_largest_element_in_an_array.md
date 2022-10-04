# [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.

Example 1:
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
```
Example 2:
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
```
Solution
```python
from collections import Counter

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mini = min(nums)
        maxi = max(nums)
        c = Counter(nums)
        curr = 0

        for i in range(maxi, mini -1, -1):
            curr += c[i]
            if curr >= k:
                return i
        return -1
```