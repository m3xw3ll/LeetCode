# [Smallest Value of the Rearranged Number](https://leetcode.com/problems/smallest-value-of-the-rearranged-number/description/)

You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any 
leading zeros.

Return the rearranged number with minimal value.

Note that the sign of the number does not change after rearranging the digits.

Example 1:
```
Input: num = 310
Output: 103
Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. 
The arrangement with the smallest value that does not contain any leading zeros is 103.
```
Example 2:
```
Input: num = -7605
Output: -7650
Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
The arrangement with the smallest value that does not contain any leading zeros is -7650.
```
Solution
```python
class Solution:
    def smallestNumber(self, num: int) -> int:
      if num == 0:
        return 0
        
      out = ''
      zero = ''

      for n in str(num):
          if n != '-':
              if n == '0':
                  zero += n
              else:
                  out += n
      out = ''.join(sorted(out))

      if num < 0:
          return -1 * int(out[::-1] + zero)
      elif out and zero:
          return int(out[0] + zero + out[1:])
      else:
          return int(out)
```