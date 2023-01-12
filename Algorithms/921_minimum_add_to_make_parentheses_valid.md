# [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/description/)

A parentheses string is valid if and only if:

- It is the empty string,
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

Example 1:
```
Input: s = "())"
Output: 1
```
Example 2:
```
Input: s = "((("
Output: 3
```
Solution
```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        lookup = {')': '('}
        stack = []
        i = 0

        while i < len(s):
            if stack and stack[-1] == lookup.get(s[i], None):
                stack.pop()
            else:
                stack.append(s[i])
            i += 1
        return len(stack)
```