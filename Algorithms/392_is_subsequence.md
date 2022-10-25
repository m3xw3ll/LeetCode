# [Is Subsequence](https://leetcode.com/problems/is-subsequence/)

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the 
characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
```
Input: s = "abc", t = "ahbgdc"
Output: true
```
Example 2:
```
Input: s = "axc", t = "ahbgdc"
Output: false
```
Solution
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = t_pointer = 0
        while len(s) > s_pointer and len(t) > t_pointer:
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                t_pointer += 1
            else:
                t_pointer += 1
        if s_pointer == len(s):
            return True
        return False
```
