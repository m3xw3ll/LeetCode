# [Determine Color of a Chessboard Square](https://leetcode.com/problems/determine-color-of-a-chessboard-square/)

You are given coordinates, a string that represents the coordinates of a square of the chessboard. Below is a chessboard
for your reference.

![](https://assets.leetcode.com/uploads/2021/02/19/screenshot-2021-02-20-at-22159-pm.png)

Return true if the square is white, and false if the square is black.

The coordinate will always represent a valid chessboard square. The coordinate will always have the letter first, and 
the number second.

Example 1:
```
Input: coordinates = "a1"
Output: false
Explanation: From the chessboard above, the square with coordinates "a1" is black, so return false.
```
Example 2:
```
Input: coordinates = "h3"
Output: true
Explanation: From the chessboard above, the square with coordinates "h3" is white, so return true.
```
Example 3:
```
Input: coordinates = "c7"
Output: false
```
Solution
```python
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        if coordinates[0] in ['a', 'c', 'e', 'g'] and int(coordinates[1]) % 2 == 0:
            return True
        if coordinates[0] in ['b', 'd', 'f', 'h'] and int(coordinates[1]) % 2 != 0:
            return True
        return False
```
