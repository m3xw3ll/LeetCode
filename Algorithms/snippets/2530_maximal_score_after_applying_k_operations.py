import heapq


def max_k_elements(nums, k):
    nums = [-1 * i for i in nums]
    heapq.heapify(nums)
    out = 0
    for i in range(k):
        max_el = -heapq.heappop(nums)
        heapq.heappush(nums, -max_el // 3)
        out += max_el
    return out


print(max_k_elements(nums=[1, 10, 3, 3, 3], k=3))
