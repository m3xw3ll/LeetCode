# [Count Vowel Substrings of a String](https://leetcode.com/problems/count-vowel-substrings-of-a-string/)

A substring is a contiguous (non-empty) sequence of characters within a string.

A vowel substring is a substring that only consists of vowels ('a', 'e', 'i', 'o', and 'u') and has all five vowels 
present in it.

Given a string word, return the number of vowel substrings in word.

Example 1:
```
Input: word = "aeiouu"
Output: 2
Explanation: The vowel substrings of word are as follows (underlined):
- "aeiouu"
- "aeiouu"
```
Example 2:
```
Input: word = "unicornarihan"
Output: 0
Explanation: Not all 5 vowels are present, so there are no vowel substrings.
```
Example 3:
```
Input: word = "cuaieuouac"
Output: 7
Explanation: The vowel substrings of word are as follows (underlined):
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
```
Solution
```python
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        cnt = 0
        vowels = set('aeiou')

        for i in range(len(word)):
            tmp = set()
            for j in range(i, len(word)):
                if word[j] in vowels:
                    tmp.add(word[j])
                    if len(tmp) == 5:
                        cnt += 1
                else:
                    break
        return cnt
```
