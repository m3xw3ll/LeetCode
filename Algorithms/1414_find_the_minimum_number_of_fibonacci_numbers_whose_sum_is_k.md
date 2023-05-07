# [Find the Minimum Number of Fibonacci Numbers Whose Sum is K](https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/description/)

Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k. The same Fibonacci number 
can be used multiple times.

The Fibonacci numbers are defined as:

- F1 = 1
- F2 = 1
- Fn = Fn-1 + Fn-2 for n > 2.

It is guaranteed that for the given constraints we can always find such Fibonacci numbers that sum up to k.
 
Example 1:
```
Input: k = 7
Output: 2 
Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
For k = 7 we can use 2 + 5 = 7.
```
Example 2:
```
Input: k = 10
Output: 2 
Explanation: For k = 10 we can use 2 + 8 = 10.
```
Example 3:
```
Input: k = 19
Output: 3 
Explanation: For k = 19 we can use 1 + 5 + 13 = 19.
```
Solution
```python
class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1, 1]
        l = 2
        while fib[-1] + fib[-2] <= k:
            fib.append(fib[-1] + fib[-2])
            l += 1
        count = 0
        while l and k:
            if fib[l - 1] > k:
                l -= 1
            else:
                k -= fib[l - 1]
                count += 1
        return count
```