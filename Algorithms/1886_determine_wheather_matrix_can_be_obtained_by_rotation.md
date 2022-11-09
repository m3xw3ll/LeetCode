# [Determine Wheather Matrix Can Be Obtained By Rotation](https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/)

Given two n x n binary matrices mat and target, return true if it is possible to make mat equal to target by rotating 
mat in 90-degree increments, or false otherwise.

Example 1:

![](https://assets.leetcode.com/uploads/2021/05/20/grid3.png)

```
Input: mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise to make mat equal target.
```
Example 2:

![](https://assets.leetcode.com/uploads/2021/05/20/grid4.png)

```
Input: mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
Output: false
Explanation: It is impossible to make mat equal to target by rotating mat.
```
Example 3:

![](https://assets.leetcode.com/uploads/2021/05/26/grid4.png)

```
Input: mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
Output: true
Explanation: We can rotate mat 90 degrees clockwise two times to make mat equal target.
```
Solution
```python
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        cnt = 0
        while cnt < 4:
            if mat == target:
                return True
            mat = [list(x) for x in (zip(*mat[::-1]))]
            cnt += 1
        return False
```