# [Letter Tile Possibilities](https://leetcode.com/problems/letter-tile-possibilities/description/)

You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

Example 1:
```
Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
```
Example 2:
```
Input: tiles = "AAABBC"
Output: 188
```
Example 3:
```
Input: tiles = "V"
Output: 1
```
Solution
```python
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def dfs(path, t, s):
            if path not in s:
                s.add(path)
                for i in range(len(t)):
                    dfs(path+t[i], t[:i] + t[i+1:], s)
            return len(s) - 1
        return dfs('', tiles, set())
```