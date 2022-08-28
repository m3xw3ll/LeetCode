# [Thousand Separator](https://leetcode.com/problems/thousand-separator/)

Given an integer n, add a dot (".") as the thousands separator and return it in string format.

Example 1:
```
Input: n = 987
Output: "987"
```
Example 2:
```
Input: n = 1234
Output: "1.234"
```
Solution
```python
class Solution:
    def thousandSeparator(self, n: int) -> str:
        if len(str(n)) <= 3:
            return str(n)
        n = str(n)[::-1]
        out = []
        for i in range(0, len(n), 3):
            out.append(n[i:i+3])
        return '.'.join(out)[::-1]
```