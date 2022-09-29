# [N-Repeated Element in Size 2N Array](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/)

You are given an integer array nums with the following properties:

- nums.length == 2 * n.
- nums contains n + 1 unique elements.
- Exactly one element of nums is repeated n times.

Return the element that is repeated n times.

Example 1:
```
Input: nums = [1,2,3,3]
Output: 3
```
Example 2:
```
Input: nums = [2,1,2,5,3,2]
Output: 2
```
Example 3:
```
Input: nums = [5,1,5,2,5,3,5,4]
Output: 5
```
Solution
```python
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1

        for k, v in dic.items():
            if v == len(nums) // 2:
                return k
```