import random
import math


class Solution:
    def __init__(self, radius, x_center, y_center):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def rand_point(self):
        alpha = 2 * math.pi * random.random()
        r = self.radius * math.sqrt(random.random())
        return r * math.cos(alpha) + self.x_center, r * math.sin(alpha) + self.y_center


if __name__ == '__main__':
    s = Solution(1.0, 0, 0)
    print(s.rand_point())
    print(s.rand_point())
    print(s.rand_point())
