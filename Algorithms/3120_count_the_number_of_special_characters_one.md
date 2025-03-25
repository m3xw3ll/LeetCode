# [Count the Number of Special Characters I](https://leetcode.com/problems/count-the-number-of-special-characters-i/description/)

You are given a string word. A letter is called special if it appears both in lowercase and uppercase in word.

Return the number of special letters in word.

Example 1:
```
Input: word = "aaAbcBC"

Output: 3

Explanation:

The special characters in word are 'a', 'b', and 'c'.
```
Example 2:
```
Input: word = "abc"

Output: 0

Explanation:

No character in word appears in uppercase.
```
Example 3:
```
Input: word = "abBCab"

Output: 1

Explanation:

The only special character in word is 'b'.
```
Solution
```python
class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        characters = list(map(chr, range(97, 123)))
        cnt = 0
        for char in characters:
            if char in word and char.upper() in word:
                cnt += 1
        return cnt
```