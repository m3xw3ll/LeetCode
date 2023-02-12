# [Longest Nice Substring](https://leetcode.com/problems/longest-nice-substring/description/)

A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. 
For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' 
appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the 
earliest occurrence. If there are none, return an empty string.

Example 1:
```
Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
```
Example 2:
```
Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
```
Example 3:
```
Input: s = "c"
Output: ""
Explanation: There are no nice substrings.
```
Solution
```python
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2: return ""
        chars = set(list(s))

        for i in range(len(s)):
            if s[i].swapcase() not in chars:
                s1 = self.longestNiceSubstring(s[:i])
                s2 = self.longestNiceSubstring(s[i+1:])
                return s2 if len(s2) > len(s1) else s1
        return s
```