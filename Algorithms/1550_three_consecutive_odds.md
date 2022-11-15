# [Three Consecutive Odds](https://leetcode.com/problems/three-consecutive-odds/)

Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

Example 1:
```
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.
```
Example 2:
```
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5,7,23] are three consecutive odds.
```
Solution
```python
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if all(x % 2 != 0 for x in arr[i:i + 3]):
                return True
        return False
```