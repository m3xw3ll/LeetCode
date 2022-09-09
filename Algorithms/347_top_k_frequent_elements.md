# [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any 
order.

Example 1:
```
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
```
Example 2:
```
Input: nums = [1], k = 1
Output: [1]
```
Solution
```python
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        freq = dict(nums.most_common(k))
        return list(freq.keys())
```
