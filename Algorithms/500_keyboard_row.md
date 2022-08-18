# [Keyboard Row](https://leetcode.com/problems/keyboard-row/)

Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

- the first row consists of the characters "qwertyuiop",
- the second row consists of the characters "asdfghjkl", and
- the third row consists of the characters "zxcvbnm".

Example 1:
```
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
```
Example 2:
```
Input: words = ["omk"]
Output: []
```
Example 3:
```
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
```
Solution
```python
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first = set('qwertyuiop')
        second = set('asdfghjkl')
        third = set('zxcvbnm')

        return [word for word in words if 
                set(word.lower()).issubset(first) or 
                set(word.lower()).issubset(second) or 
                set(word.lower()).issubset(third)]
```