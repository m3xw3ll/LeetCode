# [Four Divisors](https://leetcode.com/problems/four-divisors/description/)

Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. 
If there is no such integer in the array, return 0.

Example 1:
```
Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.
```
Example 2:
```
Input: nums = [21,21]
Output: 64
```
Example 3:
```
Input: nums = [1,2,3,4,5]
Output: 0
```
Solution
```python
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        s = 0
        for n in nums:
            tmp = set()
            for i in range(1, int(n ** 0.5) + 1):
                if n % i == 0:
                    tmp.add(i)
                    tmp.add(n // i)
                if len(tmp) > 4:
                    break
            if len(tmp) == 4:
                s += sum(tmp)
        return s
```