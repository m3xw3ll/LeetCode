# [Valid Perfect Square](https://leetcode.com/problems/valid-perfect-square/)

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.

Example 1:
```
Input: num = 16
Output: true
```
Example 2:
```
Input: num = 14
Output: false
```
Solution
```python
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num

        while left <= right:
            middle = (left + right) // 2
            if middle * middle > num:
                right = middle - 1
            elif middle * middle < num:
                left = middle + 1
            else:
                return True
        return False
```