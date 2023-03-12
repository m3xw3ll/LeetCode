# [Sum of Square Numbers](https://leetcode.com/problems/sum-of-square-numbers/description/)

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
```
Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
```
Example 2:
```
Input: c = 3
Output: false
```
Solution
```python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        root = int(c ** 0.5)
        left = 0
        right = root

        while left <= right:
            res = left ** 2 + right ** 2

            if res == c:
                return True
            elif res > c:
                right -= 1
            else:
                left += 1

        return False
```