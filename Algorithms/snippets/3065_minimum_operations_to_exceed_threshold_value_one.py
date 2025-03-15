import heapq


def min_operations(nums, k):
    cnt = 0
    heapq.heapify(nums)
    while nums and nums[0] < k:
        heapq.heappop(nums)
        cnt += 1
    return cnt


print(min_operations(nums=[2, 11, 10, 1, 3], k=10))
