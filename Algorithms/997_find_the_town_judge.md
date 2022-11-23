# [Find the Town Judge](https://leetcode.com/problems/find-the-town-judge/)

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Example 1:
```
Input: n = 2, trust = [[1,2]]
Output: 2
```
Example 2:
```
Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
```
Example 3:
```
Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
```
Solution
```python
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * (n + 1)
        for a, b in trust:
            trusted[a] -= 1
            trusted[b] += 1

        for i in range(1, len(trusted)):
            if trusted[i] == n-1:
                return i
        return -1
```
