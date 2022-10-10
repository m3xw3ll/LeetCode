# [Find and Replace Pattern](https://leetcode.com/problems/find-and-replace-pattern/)

Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the 
answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the 
pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and 
no two letters map to the same letter.

Example 1:
```
Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
```
Example 2:
```
Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]
```
Solution
```python
class Solution:
    def make_pattern(self, word):
        dic = {}
        p = list()
        cnt = 0

        for char in word:
            if char not in dic:
                dic[char] = cnt
                cnt += 1
            p.append(dic[char])
        return p
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        pat = self.make_pattern(pattern)
        return [word for word in words if self.make_pattern(word) == pat]
        
```