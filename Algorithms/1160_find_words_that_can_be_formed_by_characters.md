# [Find Words That Can Be Formed by Characters](https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/)

You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

Example 1:
```
Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
```
Example 2:
```
Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
```
Solution
```python
from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt = 0
        chars = Counter(chars)
        for word in words:
            tmp = Counter(word)
            k = 0
            for c in word:
                if chars[c] < tmp[c]:
                    k = 1
                    continue
            if k == 0:
                cnt += len(word)
        return cnt
```