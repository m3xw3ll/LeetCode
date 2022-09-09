# [Binary Number with Alternating Bits](https://leetcode.com/problems/binary-number-with-alternating-bits/)

Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different
values.

Example 1:
```
Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101
```
Example 2:
```
Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.
```
Example 3:
```
Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.
```
Solution
```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit = format(n, 'b')
        first = bit[0]
        for b in range(1, len(bit)):
            if bit[b] == first:
                return False
            else:
                first = bit[b]
        return True
```