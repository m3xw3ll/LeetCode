# [Generate Random Point in a Circle](https://leetcode.com/problems/generate-random-point-in-a-circle/description/)

Given the radius and the position of the center of a circle, implement the function randPoint which generates a uniform 
random point inside the circle.

Implement the Solution class:

- Solution(double radius, double x_center, double y_center) initializes the object with the radius of the circle radius 
and the position of the center (x_center, y_center).
- randPoint() returns a random point inside the circle. A point on the circumference of the circle is considered to be in 
the circle. The answer is returned as an array [x, y].
  
Example 1:
```
Input
["Solution", "randPoint", "randPoint", "randPoint"]
[[1.0, 0.0, 0.0], [], [], []]
Output
[null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]

Explanation
Solution solution = new Solution(1.0, 0.0, 0.0);
solution.randPoint(); // return [-0.02493, -0.38077]
solution.randPoint(); // return [0.82314, 0.38945]
solution.randPoint(); // return [0.36572, 0.17248]
```
Solution
```python
import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        

    def randPoint(self) -> List[float]:
        alpha = 2 * math.pi * random.random()
        r = self.radius * math.sqrt(random.random())
        return r * math.cos(alpha) + self.x_center, r * math.sin(alpha) + self.y_center


if __name__ == '__main__':
    s = Solution(1.0, 0, 0)
    print(s.randPoint())
    print(s.randPoint())
    print(s.randPoint())
```