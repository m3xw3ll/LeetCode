# [Find Common Characters](https://leetcode.com/problems/find-common-characters/)

Given a string array words, return an array of all characters that show up in all strings within the words 
(including duplicates). You may return the answer in any order.

Example 1:
```
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
```
Example 2:
```
Input: words = ["cool","lock","cook"]
Output: ["c","o"]
```
Solution
```python
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        out = []
        d = {}
        for s in set(words[0]):
            d[s] = min([word.count(s) for word in words])
        for k, v in d.items():
            out += [k] * v
        return out
```