# [Ugly Number](https://leetcode.com/problems/ugly-number/)

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

Example 1:
```
Input: n = 6
Output: true
Explanation: 6 = 2 × 3
```
Example 2:
```
Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
```
Example 3:
```
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.
```
Solution
```python
class Solution:
    def isUgly(self, n: int) -> bool:
        primes = [2, 3, 5]
        if n == 0:
            return False
        for p in primes:
            while n % p == 0:
                n = n // p
        return n == 1
```