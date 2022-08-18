# [To Lower Case](https://leetcode.com/problems/to-lower-case/)

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example 1:
```
Input: s = "Hello"
Output: "hello"
```
Example 2:
```
Input: s = "here"
Output: "here"
```
Example 3:
```
Input: s = "LOVELY"
Output: "lovely"
```
Solution
```python
class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.lower()
```