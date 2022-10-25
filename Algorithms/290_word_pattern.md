# [Word Pattern](https://leetcode.com/problems/word-pattern/)

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
```
Input: pattern = "abba", s = "dog cat cat dog"
Output: true
```
Example 2:
```
Input: pattern = "abba", s = "dog cat cat fish"
Output: false
```
Example 3:
```
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
```
Solution
```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False

        dic = {}
        for a, b in zip(pattern, s):
            if a in dic and dic[a] != b:
                return False
            dic[a] = b
        if len(set(dic.keys())) != len(set(dic.values())):
            return False
        return True
```