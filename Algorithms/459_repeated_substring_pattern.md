# [Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/description/)

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the 
substring together.

Example 1:
```
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
```
Example 2:
```
Input: s = "aba"
Output: false
```
Example 3:
```
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
```
Solution
```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        l = len(s)
        for i in range(0, l // 2):
            ss = s[0:i+1]
            if ss * (len(s) // len(ss)) == s:
                return True
        return False
```