# [Sort Array By Parity](https://leetcode.com/problems/sort-array-by-parity/)

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:
```
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```
Example 2:
```
Input: nums = [0]
Output: [0]
```
Solution
```python
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        out = []
        for x in nums:
            if x % 2 == 0:
                out.append(x)
        for y in nums:
            if y % 2 != 0:
                out.append(y)
        return out
```