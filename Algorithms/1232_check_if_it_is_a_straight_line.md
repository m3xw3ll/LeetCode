# [Check If It Is a Straight Line](https://leetcode.com/problems/check-if-it-is-a-straight-line/)

You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if
these points make a straight line in the XY plane.

![](https://assets.leetcode.com/uploads/2019/10/15/untitled-diagram-2.jpg)

```
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
```

![](https://assets.leetcode.com/uploads/2019/10/09/untitled-diagram-1.jpg)

```
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
```

Solution
```python
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1) = coordinates[0]
        (x2, y2) = coordinates[1]

        for (x3, y3) in coordinates[2:]:
            if (y2 - y1) * (x3 - x1) != (y3 - y1) * (x2 - x1):
                return False
        return True
```