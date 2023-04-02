# [Form Smallest Number From Two Digit Arrays](https://leetcode.com/problems/form-smallest-number-from-two-digit-arrays/description/)

Given two arrays of unique digits nums1 and nums2, return the smallest number that contains at least one digit from each array.

Example 1:
```
Input: nums1 = [4,1,3], nums2 = [5,7]
Output: 15
Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be proven that 15 is the smallest number we can have.
```
Example 2:
```
Input: nums1 = [3,5,2,6], nums2 = [3,1,7]
Output: 3
Explanation: The number 3 contains the digit 3 which exists in both arrays.
```
Solution
```python
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        nums1 = set(nums1)
        nums2 = set(nums2)

        both = nums1.intersection(nums2)
        if len(both) >= 1:
            return sorted(list(both))[0]

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        n1, n2 = min(nums1), min(nums2)
        return min(n1, n2) * 10 + max(n1, n2)
```