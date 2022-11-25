# [Longest Palindrome](https://leetcode.com/problems/longest-palindrome/)

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that 
can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
```
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
```
Example 2:
```
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
```
Solution
```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        odd = 0
        out = 0
        for c in s:
            if c not in dic:
                dic[c] = 1
            else:
                dic[c] += 1

        for f in dic.values():
            out += f
            if f % 2 != 0:
                odd += 1
        if odd == 0:
            return out - odd
        else:
            return out - odd + 1
```
