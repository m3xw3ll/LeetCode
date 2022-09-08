# [Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a 
backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:
```
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
```
Example 2:
```
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
```
Example 3:
```
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
```
Solution
```python
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss = []
        tt = []

        for i in range(len(s)):
            if s[i] != '#':
                ss.append(s[i])
            if s[i] == '#' and len(ss) > 0:
                ss.pop()

        for j in range(len(t)):
            if t[j] != '#':
                tt.append(t[j])
            if t[j] == '#' and len(tt) > 0:
                tt.pop()

        return True if ss == tt else False
```