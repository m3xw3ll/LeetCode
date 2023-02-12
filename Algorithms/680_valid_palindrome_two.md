# [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/description/)

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
```
Input: s = "aba"
Output: true
```
Example 2:
```
Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
```
Example 3:
```
Input: s = "abc"
Output: false
```
Solution
```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        def helper(s, i, j):
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return helper(s, i + 1, j) or helper(s, i, j - 1)
        return True
```