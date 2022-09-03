# [Strong Password Checker II](https://leetcode.com/problems/strong-password-checker-ii/)

A password is said to be strong if it satisfies all the following criteria:

- It has at least 8 characters.
- It contains at least one lowercase letter.
- It contains at least one uppercase letter.
- It contains at least one digit.
- It contains at least one special character. The special characters are the characters in the following string: 
``"!@#$%^&*()-+"``.
- It does not contain 2 of the same character in adjacent positions (i.e., "aab" violates this condition, but "aba" 
does not).
  

Given a string password, return true if it is a strong password. Otherwise, return false.

Example 1:
```
Input: password = "IloveLe3tcode!"
Output: true
Explanation: The password meets all the requirements. Therefore, we return true.
```
Example 2:
```
Input: password = "Me+You--IsMyDream"
Output: false
Explanation: The password does not contain a digit and also contains 2 of the same character in adjacent positions. 
Therefore, we return false.
```
Example 3:
```
Input: password = "1aB!"
Output: false
Explanation: The password does not meet the length requirement. Therefore, we return false.
```
Solution
```python
class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        has_lower = False
        has_upper = False
        has_digit = False
        has_special = False
        specials = '"!@#$%^&*()-+"'
        if len(password) < 8:
            return False
        for char in range(len(password)):
            if password[char].islower():
                has_lower = True
            if password[char].isupper():
                has_upper = True
            if password[char].isdigit():
                has_digit = True
            if password[char] in specials:
                has_special = True

        for char in range(1, len(password)):
            if password[char] == password[char-1]:
                return False
        if has_lower and has_upper and has_digit and has_special:
            return True
        return False
```