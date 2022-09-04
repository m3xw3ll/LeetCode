# [XOR Operation in an Array](https://leetcode.com/problems/xor-operation-in-an-array/)

You are given an integer n and an integer start.

Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.

Example 1:
```
Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.
```
Example 2:
```
Input: n = 4, start = 3
Output: 8
Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.
```
Solution
```python
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        out = 0
        nums = [i for i in range(start, start + 2 * (n), 2)]
        for n in nums:
            out ^= n
        return out
```