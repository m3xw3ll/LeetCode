# [Count Primes](https://leetcode.com/problems/count-primes/)

Given an integer n, return the number of prime numbers that are strictly less than n.

Example 1:
```
Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
```
Example 2:
```
Input: n = 0
Output: 0
```
Example 3:
```
Input: n = 1
Output: 0
```
Solution
```python
class Solution:
    def countPrimes(self, n: int) -> int:
        seen = [0] * n
        out = 0
        for num in range(2, n):
            if seen[num]:
                continue
            out += 1
            seen[num*num:n:num] = [1] * ((n - 1) // num - num +1)
        return out
```