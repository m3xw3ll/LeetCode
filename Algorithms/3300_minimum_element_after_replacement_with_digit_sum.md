# [Minimum Element After Replacement With Digit Sum](https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum/description/)

You are given an integer array nums.

You replace each element in nums with the sum of its digits.

Return the minimum element in nums after all replacements.

Example 1:
```
Input: nums = [10,12,13,14]

Output: 1

Explanation:

nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.
```
Example 2:
```
Input: nums = [1,2,3,4]

Output: 1

Explanation:

nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.
```
Example 3:
```
Input: nums = [999,19,199]

Output: 10

Explanation:

nums becomes [27, 10, 19] after all replacements, with minimum element 10.
```
Solution
```python
class Solution:
    def minElement(self, nums: List[int]) -> int:
        m = float('inf')
        for n in nums:
            digs_sum = sum(int(x) for x in str(n))
            m = min(m, digs_sum)
        return m
```