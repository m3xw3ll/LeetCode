# [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
```
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
```
Example 2:
```
Input: n = 1
Output: ["()"]
```
Solution
```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        out = []

        def backtrack(n_open, n_close):
            if n_open == n_close == n:
                out.append(''.join(stack))
                return

            if n_open < n:
                stack.append('(')
                backtrack(n_open + 1, n_close)
                stack.pop()

            if n_close < n_open:
                stack.append(')')
                backtrack(n_open, n_close + 1)
                stack.pop()

        backtrack(0, 0)
        return out
```
