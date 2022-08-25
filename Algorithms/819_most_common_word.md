# [Most Common Word](https://leetcode.com/problems/most-common-word/)

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not 
banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

Example 1:
```
Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
```
Example 2:
```
Input: paragraph = "a.", banned = []
Output: "a"
```
Solution
```python
from collections import Counter, OrderedDict
import regex as re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = " ".join(re.findall(r"[a-zA-Z0-9]+", paragraph))
        c = Counter(paragraph.lower().split())
        c = OrderedDict(c.most_common())
        for word in c:
            if word not in banned:
                return word
```