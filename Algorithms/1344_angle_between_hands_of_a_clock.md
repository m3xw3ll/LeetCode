# [Angle Between Hands of a Clock](https://leetcode.com/problems/angle-between-hands-of-a-clock/description/)

Given two numbers, hour and minutes, return the smaller angle (in degrees) formed between the hour and the minute hand.

Answers within 10-5 of the actual value will be accepted as correct.

Example 1:

![](https://assets.leetcode.com/uploads/2019/12/26/sample_1_1673.png)

```
Input: hour = 12, minutes = 30
Output: 165
```
Example 2:

![](https://assets.leetcode.com/uploads/2019/12/26/sample_2_1673.png)

```
Input: hour = 3, minutes = 30
Output: 75
```
Example 3:

![](https://assets.leetcode.com/uploads/2019/12/26/sample_3_1673.png)

```
Input: hour = 3, minutes = 15
Output: 7.5
```
Solution
```python
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minutes_hand = minutes * 6
        hour_hand = (hour % 12 * 30) + minutes / 60 * 30
        angle = abs(hour_hand - minutes_hand)
        return 360 - angle if angle > 180 else angle
```