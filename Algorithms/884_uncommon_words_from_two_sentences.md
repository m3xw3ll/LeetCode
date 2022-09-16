# [Uncommon Words from Two Sentences](https://leetcode.com/problems/uncommon-words-from-two-sentences/)

A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

Example 1:
```
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
```
Example 2:
```
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]
```
Solution
```python
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ss = s1.split() + s2.split()
        d = {}
        for w in ss:
            if w in d:
                d[w] += 1
            else:
                d[w] = 1

        return [w for w in d if d[w] == 1]
```
