# [Sort Array By Parity II](https://leetcode.com/problems/sort-array-by-parity-ii/)

Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

Return any answer array that satisfies this condition.

Example 1:
```
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
```
Example 2:
```
Input: nums = [2,3]
Output: [2,3]
```
Solution
```python
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        out = [0] * len(nums)
        evens = list()
        odds = list()

        for n in nums:
            if n % 2 == 0:
                evens.append(n)
            else:
                odds.append(n)

        for i in range(len(out)):
            if i % 2 == 0:
                out[i] = evens.pop()
            else:
                out[i] = odds.pop()
        return out
```