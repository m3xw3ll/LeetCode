# [Peak index in a Mountain Array](https://leetcode.com/problems/peak-index-in-a-mountain-array/description/)

An array arr a mountain if the following properties hold:

- arr.length >= 3
- There exists some i with 0 < i < arr.length - 1 such that:
    - arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
    - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Given a mountain array arr, return the index i such that arr[0] < arr[1] < ... < arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

You must solve it in O(log(arr.length)) time complexity.

Example 1:
```
Input: arr = [0,1,0]
Output: 1
```
Example 2:
```
Input: arr = [0,2,1,0]
Output: 1
```
Example 3:
```
Input: arr = [0,10,5,2]
Output: 1
```
Solution
```python
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        while l < r:
            m = (l + r) // 2
            if arr[m] < arr[m + 1]:
                l = m + 1
            else:
                r = m
        return l
```