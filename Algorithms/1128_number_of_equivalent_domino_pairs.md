# [Number of Equivalent Domino Pairs](https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/)

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either 
(a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

Example 1:
```
Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
```
Example 2:
```
Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
```
Solution
```python
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dict = defaultdict(int)
        out = 0
        for d1, d2 in dominoes:
            k = min(d1, d2), max(d1, d2)
            out += dict[k]
            dict[k] += 1
        return out
```