import random


class Solution:
    def __init__(self, nums):
        self.nums = nums[:]
        self.copy = nums[:]

    def reset(self):
        self.nums = self.copy[:]
        return self.nums

    def shuffle(self):
        for i in range(len(self.nums)):
            j = random.randint(i, len(self.nums) - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums


if __name__ == '__main__':
    s = Solution([1, 2, 3])
    print(s.shuffle())
    print(s.reset())
