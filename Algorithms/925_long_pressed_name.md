# [Long Pressed Name](https://leetcode.com/problems/long-pressed-name/description/)

Your friend is typing his name into a keyboard. Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard. Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

Example 1:
```
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed.
```
Example 2:
```
Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must have been pressed twice, but it was not in the typed output.
```
Solution
```python
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        ni = 0
        ti = 0
        while ni <= len(name) and ti < len(typed):
            if ni < len(name) and typed[ti] == name[ni]:
                ti += 1
                ni += 1
            elif typed[ti] == name[ni - 1] and ni != 0:
                ti += 1
            else:
                return False
        return ni == len(name) and ti == len(typed)
```