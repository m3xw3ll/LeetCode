# [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1) Open brackets must be closed by the same type of brackets.
2) Open brackets must be closed in the correct order.
3) Every close bracket has a corresponding open bracket of the same type.

Example 1:
```
Input: s = "()"
Output: true
```
Example 2:
```
Input: s = "()[]{}"
Output: true
```
Example 3:
```
Input: s = "(]"
Output: false
```
Solution
```python
class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {'(': ')',
              '{': '}',
              '[': ']'}
        stack = []
        for i in s:
            if i in lookup:
                stack.append(i)
            elif len(stack) == 0 or lookup[stack.pop()] != i:
                return False
        return len(stack) == 0
```
