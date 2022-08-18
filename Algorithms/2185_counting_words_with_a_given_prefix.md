# [Counting Words With a Given Prefix](https://leetcode.com/problems/counting-words-with-a-given-prefix/)

You are given an array of strings words and a string pref.

Return the number of strings in words that contain pref as a prefix.

A prefix of a string s is any leading contiguous substring of s.

Example 1:
```
Input: words = ["pay","attention","practice","attend"], pref = "at"
Output: 2
Explanation: The 2 strings that contain "at" as a prefix are: "attention" and "attend".
```
Example 2:
```
Input: words = ["leetcode","win","loops","success"], pref = "code"
Output: 0
Explanation: There are no strings that contain "code" as a prefix.
```
Solution
```python
class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        cnt = 0
        for word in words:
            if len(word) >= len(pref):
                if word[0:len(pref)] == pref:
                    cnt += 1
        return cnt
```