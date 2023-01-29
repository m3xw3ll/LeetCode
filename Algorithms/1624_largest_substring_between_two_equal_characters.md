# [Largest Substring Between Two Equal Characters](https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/)

Given a string s, return the length of the longest substring between two equal characters, excluding the two characters.
If there is no such substring return -1.

A substring is a contiguous sequence of characters within a string.

Example 1:
```
Input: s = "aa"
Output: 0
Explanation: The optimal substring here is an empty substring between the two 'a's.
```
Example 2:
```
Input: s = "abca"
Output: 2
Explanation: The optimal substring here is "bc".
```
Example 3:
```
Input: s = "cbzxy"
Output: -1
Explanation: There are no characters that appear twice in s.
```
Solution
```python
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        dic = {}
        dist = -1

        for idx, char in enumerate(s):
            if char not in dic:
                dic[char] = idx
            else:
                dist = max(dist, idx - dic[char] - 1)
        return dist
```