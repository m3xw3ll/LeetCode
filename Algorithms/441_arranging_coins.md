# [Arranging Coins](https://leetcode.com/problems/arranging-coins/)

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row 
has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:

![](https://assets.leetcode.com/uploads/2021/04/09/arrangecoins1-grid.jpg)

```
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
```
Example 2:

![](https://assets.leetcode.com/uploads/2021/04/09/arrangecoins2-grid.jpg)

```
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
```
Solution
```
class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 1
        stair = 0
        while i <= n:
            stair += 1
            n -= i
            i += 1
        return stair
```