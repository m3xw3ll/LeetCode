# [Add Binary](https://leetcode.com/problems/add-binary/)

Given two binary strings a and b, return their sum as a binary string.

Example 1:
```
Input: a = "11", b = "1"
Output: "100"
```

Example 2:
```
Input: a = "1010", b = "1011"
Output: "10101"
```

Solution:
```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return format(int(a, 2) + int(b, 2), 'b')
```