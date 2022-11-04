# [Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)

Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding 
column number.

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
Input: columnTitle = "A"
Output: 1
```
Example 2:
```
Input: columnTitle = "AB"
Output: 28
```
Example 3:
```
Input: columnTitle = "ZY"
Output: 701
```
Solution
```python
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        s = 0
        for i in columnTitle:
            s = s * 26 + (ord(i)) - ord('A') + 1
        return s
```