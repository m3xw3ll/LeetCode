# [Path Crossing](https://leetcode.com/problems/path-crossing/)

Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or 
west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously 
visited. Return false otherwise.


Example 1:

![](https://assets.leetcode.com/uploads/2020/06/10/screen-shot-2020-06-10-at-123929-pm.png)

```
Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.
```
Example 2:

![](https://assets.leetcode.com/uploads/2020/06/10/screen-shot-2020-06-10-at-123843-pm.png)

```
Input: path = "NESWW"
Output: true
Explanation: Notice that the path visits the origin twice.
```
Solution
```python
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        seen = set()
        seen.add((0,0))
        x = 0
        y = 0
        for i in path:
            if i == 'N':
                y += 1
            elif i == 'S':
                y -= 1
            elif i == 'W':
                x += 1
            elif i == 'E':
                x -= 1
            if (x, y) in seen:
                return True
            seen.add((x,y))
        return False
```