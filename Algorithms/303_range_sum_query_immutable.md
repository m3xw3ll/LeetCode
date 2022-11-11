# [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)

Given an integer array nums, handle multiple queries of the following type:

1. Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.

Implement the NumArray class:

- NumArray(int[] nums) Initializes the object with the integer array nums.
- int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive 
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).
  
Example 1:
```
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
```
Solution
```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        cnt = 0
        for i in range(left, right+1):
            cnt += self.nums[i]
        return cnt

if __name__ == '__main__':
    na = NumArray([-2, 0, 3, -5, 2, -1])
    na.sumRange(0, 2)
    na.sumRange(2, 5)
    na.sumRange(0, 5)
```