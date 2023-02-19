# [Prit Words Vertically](https://leetcode.com/problems/print-words-vertically/description/)

Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

Example 1:
```
Input: s = "HOW ARE YOU"
Output: ["HAY","ORO","WEU"]
Explanation: Each word is printed vertically. 
 "HAY"
 "ORO"
 "WEU"
 ```
Example 2:
```
Input: s = "TO BE OR NOT TO BE"
Output: ["TBONTB","OEROOE","   T"]
Explanation: Trailing spaces is not allowed. 
"TBONTB"
"OEROOE"
"   T"
```
Example 3:
```
Input: s = "CONTEST IS COMING"
Output: ["CIC","OSO","N M","T I","E N","S G","T"]
```
Solution
```python
from itertools import zip_longest

class Solution:
    def printVertically(self, s: str) -> List[str]:
        out = list()
        for x in zip_longest(*s.split(), fillvalue=' '):
            out.append(''.join(x))
        return [x.rstrip() for x in out]
```