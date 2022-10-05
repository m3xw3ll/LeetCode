# [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
```
Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```
Example 3:
```
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
```
Solution
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = ''
        out = 0

        for i in range(len(s)):
            if s[i] in word:
                out = max(len(word), out)
                idx = word.index(s[i])
                word = word[idx+1:]
            word += s[i]
        return max(len(word), out)
```
