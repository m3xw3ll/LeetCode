# [Redistribute Characters to Make All Strings Equal](https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/)

You are given an array of strings words (0-indexed).

In one operation, pick two distinct indices i and j, where words[i] is a non-empty string, and move any character from 
words[i] to any position in words[j].

Return true if you can make every string in words equal using any number of operations, and false otherwise.

Example 1:
```
Input: words = ["abc","aabc","bc"]
Output: true
Explanation: Move the first 'a' in words[1] to the front of words[2],
to make words[1] = "abc" and words[2] = "abc".
All the strings are now equal to "abc", so return true.
```
Example 2:
```
Input: words = ["ab","a"]
Output: false
Explanation: It is impossible to make all the strings equal using the operation.
```
Solution
```python
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        chars = ''.join(words)
        dist_chars = set(chars)

        for char in dist_chars:
            if chars.count(char) % len(words) != 0:
                return False
        return True
```