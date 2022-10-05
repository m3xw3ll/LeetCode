# [String Matching in an Array](https://leetcode.com/problems/string-matching-in-an-array/)

Given an array of string words. Return all strings in words which is substring of another word in any order. 

String words[i] is substring of words[j], if can be obtained removing some characters to left and/or right side of words[j].

Example 1:
```
Input: words = ["mass","as","hero","superhero"]
Output: ["as","hero"]
Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
["hero","as"] is also a valid answer.
```
Example 2:
```
Input: words = ["leetcode","et","code"]
Output: ["et","code"]
Explanation: "et", "code" are substring of "leetcode".
```
Example 3:
```
Input: words = ["blue","green","bu"]
Output: []
```
Solution
```python
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        sorted_words = sorted(words, key=len)
        out = []

        for i in range(len(sorted_words)):
            for j in range(i+1, len(sorted_words)):
                if sorted_words[i] in sorted_words[j]:
                    out.append(sorted_words[i])
                    break
        return out
```