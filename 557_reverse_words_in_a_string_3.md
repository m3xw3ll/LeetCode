# [Reverse Words in a String III](https://leetcode.com/problems/reverse-words-in-a-string-iii/)

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
```
Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
```
Example 2:
```
Input: s = "God Ding"
Output: "doG gniD"
```
Solution
```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([i[::-1] for i in s.split(' ')])
```