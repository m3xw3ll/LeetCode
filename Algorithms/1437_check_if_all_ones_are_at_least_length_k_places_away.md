# [Check if All 1´s Are at Least Length K Places Away](https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/description/)

Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.

Example 1:

![](https://assets.leetcode.com/uploads/2020/04/15/sample_1_1791.png)

```
Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
```
Example 2:

![](https://assets.leetcode.com/uploads/2020/04/15/sample_2_1791.png)

```
Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
```
Solution
```python
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dst = k
        for n in nums:
            if n == 0:
                dst += 1
            elif n == 1 and dst >= k:
                dst = 0
            else:
                return False
        return True
```