# [Multiply Strings](https://leetcode.com/problems/multiply-strings/description/)

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also 
represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
```
Input: num1 = "2", num2 = "3"
Output: "6"
```
Example 2:
```
Input: num1 = "123", num2 = "456"
Output: "56088"
```
Solution
```python
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        digits = {
                '0': 0,
                '1': 1,
                '2': 2,
                '3': 3,
                '4': 4,
                '5': 5,
                '6': 6,
                '7': 7,
                '8': 8,
                '9': 9}

        v1 = 0
        v2 = 0

        for i in num1:
            v1 = 10 * v1 + digits[i]
        for j in num2:
            v2 = 10 * v2 + digits[j]

        return str(v1 * v2)
        
```