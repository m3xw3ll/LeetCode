import heapq


class KthLargest:
    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)

        while len(self.nums) > k:
            heapq.heappop(self.nums)


    def add(self, val):
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums, val)
        return self.nums[0]



if __name__ == '__main__':
    l = KthLargest(3, [4, 5, 8, 2])
    print(l.add(3))
    print(l.add(5))
    print(l.add(10))
    print(l.add(9))
    print(l.add(4))

