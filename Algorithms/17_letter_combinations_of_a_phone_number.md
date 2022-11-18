# [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could 
represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any 
letters.

![](https://assets.leetcode.com/uploads/2022/03/15/1200px-telephone-keypad2svg.png)

Example 1:
```
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```
Example 2:
```
Input: digits = ""
Output: []
```
Example 3:
```
Input: digits = "2"
Output: ["a","b","c"]
```
Solution
```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup = {'2': 'abc',
                  '3': 'def',
                  '4': 'ghi',
                  '5': 'jkl',
                  '6': 'mno',
                  '7': 'pqrs',
                  '8': 'tuv',
                  '9': 'wxyz'}

        out = list()

        def backtrack(i, curr):
            if len(digits) == len(curr):
                out.append(curr)
                return
            for c in lookup[digits[i]]:
                backtrack(i+1, curr + c)

        if digits:
            backtrack(0, '')
        return out
```
