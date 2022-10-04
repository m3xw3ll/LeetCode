# [Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/)

Given a string s, reverse the string according to the following rules:

- All the characters that are not English letters remain in the same position.
- All the English letters (lowercase or uppercase) should be reversed.

Return s after reversing it.

Example 1:
```
Input: s = "ab-cd"
Output: "dc-ba"
```
Example 2:
```
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
```
Example 3:
```
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
```
Solution
```python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        chars = set('abcdefghijklmnopqrstuvwxzyABCDEFGHIJKLMNOPQRSTUVWXYZ')
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] in chars and s[right] in chars:
                s[left], s[right] = s[right], s[left]
            elif s[left] not in chars:
                left += 1
                continue
            elif s[right] not in chars:
                right -= 1
                continue
            left += 1
            right -= 1
        return ''.join(s)
```