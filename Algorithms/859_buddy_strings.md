# [Buddy Strings](https://leetcode.com/problems/buddy-strings/description/)

Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].

- For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

Example 1:
```
Input: s = "ab", goal = "ba"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
```
Example 2:
```
Input: s = "ab", goal = "ab"
Output: false
Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b', which results in "ba" != goal.
```
Example 3:
```
Input: s = "aa", goal = "aa"
Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is equal to goal.
```
Solution
```python
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal) or sorted(s) != sorted(goal):
            return False

        cnt = 0
        rep = 0
        equals = set()
        for i, y in zip(s, goal):
            if i == y:
                if i in equals:
                    rep += 1
                else:
                    equals.add(i)
            else:
                cnt += 1
        return True if cnt == 2 or (cnt == 0 and rep) else False
```