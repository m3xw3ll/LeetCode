# [Split a String in Balanced Strings](https://leetcode.com/problems/split-a-string-in-balanced-strings/)

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.

Given a balanced string s, split it into some number of substrings such that:

- Each substring is balanced.

Return the maximum number of balanced strings you can obtain.

Example 1:
```
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.
```
Example 2:
```
Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.
```
Example 3:
```
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".
```
Solution
```python
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        out = 0
        cnt = 0

        for i in s:
            if i == 'L':
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                out += 1
        return out
```