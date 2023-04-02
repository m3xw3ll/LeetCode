# [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/)

Given an n x n matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element 
in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Example 1:
```
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13
```
Example 2:
```
Input: matrix = [[-5]], k = 1
Output: -5
```
Solution
```python
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heap.append(matrix[i][j])

        heapq.heapify(heap)
        i = 1
        while i < k:
            heapq.heappop(heap)
            i += 1
        return heap[0]
```