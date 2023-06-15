# [Least Number of Unique Integers after K Removals](https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/?envType=list&envId=eiocrakj)

Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k 
elements.

Example 1:
```
Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
```
Example 2:
```
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
```
Solution
```python
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        cnt = Counter(c.values())
        rem = len(c)
        for i in sorted(cnt):
            if k >= i * cnt[i]:
                k -= i * cnt[i]
                rem -= cnt.pop(i)
            else:
                return rem - k // i
        return rem
```