# [Length of the Longest Alphabetical Continuous Substing](https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/description/)

An alphabetical continuous string is a string consisting of consecutive letters in the alphabet. In other words, it is 
any substring of the string "abcdefghijklmnopqrstuvwxyz".

- For example, "abc" is an alphabetical continuous string, while "acb" and "za" are not.
Given a string s consisting of lowercase letters only, return the length of the longest alphabetical continuous substring.
  
Example 1:
```
Input: s = "abacaba"
Output: 2
Explanation: There are 4 distinct continuous substrings: "a", "b", "c" and "ab".
"ab" is the longest continuous substring.
```
Example 2:
```
Input: s = "abcde"
Output: 5
Explanation: "abcde" is the longest continuous substring.
```
Solution
```python
class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        out = 1
        tmp = 1
        for i in range(len(s) - 1):
            if ord(s[i]) == ord(s[i+1]) - 1:
                tmp += 1
            else:
                tmp = 1
            out = max(out, tmp)
        return out
```