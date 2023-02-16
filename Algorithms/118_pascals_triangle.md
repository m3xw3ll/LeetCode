# [Pascal´s Triangle](https://leetcode.com/problems/pascals-triangle/description/)

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

![](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)

Example 1:
```
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
```
Example 2:
```
Input: numRows = 1
Output: [[1]]
```
Solution
```python
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tmp = 0
        out = list()

        while tmp <= numRows:
            if tmp == 1:
                out.append([1])
            if tmp == 2:
                out.append([1, 1])
            if tmp > 2:
                tmp_row = out[-1]
                new_row = []
                new_row.append(1)
                for i in range(len(tmp_row) - 1):
                    new_row.append(tmp_row[i] + tmp_row[i+1])
                new_row.append(1)
                out.append(new_row)
            tmp += 1
        return out
```