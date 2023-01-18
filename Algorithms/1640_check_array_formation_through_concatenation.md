# [Check Array Formation Through Concatenation](https://leetcode.com/problems/check-array-formation-through-concatenation/description/)

You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are 
distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to 
reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.

Example 1:
```
Input: arr = [15,88], pieces = [[88],[15]]
Output: true
Explanation: Concatenate [15] then [88]
```
Example 2:
```
Input: arr = [49,18,16], pieces = [[16,18,49]]
Output: false
Explanation: Even though the numbers match, we cannot reorder pieces[0].
```
Example 3:
```
Input: arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
Output: true
Explanation: Concatenate [91] then [4,64] then [78]
```
Solution
```python
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        out = list()
        dict = {x[0]: x for x in pieces}

        for i in arr:
            out += dict.get(i, [])
        return out == arr
```