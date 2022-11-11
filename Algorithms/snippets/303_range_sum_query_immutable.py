class NumArray:
    def __init__(self, nums):
        self.nums = nums

    def sum_range(self, left, right):
        cnt = 0
        for i in range(left, right+1):
            cnt += self.nums[i]
        return cnt


if __name__ == '__main__':
    na = NumArray([-2, 0, 3, -5, 2, -1])
    print(na.sum_range(0, 2))
    print(na.sum_range(2, 5))
    print(na.sum_range(0, 5))