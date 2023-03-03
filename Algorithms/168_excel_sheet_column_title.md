# [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/description/)

Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:
```
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
```

Example 1:
```
Input: columnNumber = 1
Output: "A"
```
Example 2:
```
Input: columnNumber = 28
Output: "AB"
```
Example 3:
```
Input: columnNumber = 701
Output: "ZY"
```
Solution
```python
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = ''
        while columnNumber > 0:
            columnNumber -= 1
            out = chr(columnNumber % 26 + 65) + out
            columnNumber //= 26
        return out
```