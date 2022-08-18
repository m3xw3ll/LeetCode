# [Reverse String](https://leetcode.com/problems/reverse-string/)

Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.

 

Example 1:
```
Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
```
Example 2:
```
Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
```
Solution
```python
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        right_idx = 1
        left_idx = 1
        l = len(s)

        while right_idx + left_idx <= l:
            s[left_idx-1], s[l-right_idx] = s[l-right_idx], s[left_idx-1]
            right_idx += 1
            left_idx += 1
```