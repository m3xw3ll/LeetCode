# [Number of Even and Odd Bits](https://leetcode.com/problems/number-of-even-and-odd-bits/description/)

You are given a positive integer n.

Let even denote the number of even indices in the binary representation of n (0-indexed) with value 1.

Let odd denote the number of odd indices in the binary representation of n (0-indexed) with value 1.

Return an integer array answer where answer = [even, odd].

Example 1:
```
Input: n = 17
Output: [2,0]
Explanation: The binary representation of 17 is 10001. 
It contains 1 on the 0th and 4th indices. 
There are 2 even and 0 odd indices.
```
Example 2:
```
Input: n = 2
Output: [0,1]
Explanation: The binary representation of 2 is 10.
It contains 1 on the 1st index. 
There are 0 even and 1 odd indices.
```
Solution
```python
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        odds = 0
        evens = 0

        for idx, val in enumerate(bin(n)[2:][::-1]):
            if idx % 2 ==  0 and val == '1':
                evens += 1
            elif idx % 2 == 1 and val == '1':
                odds += 1
        return [evens, odds]
```