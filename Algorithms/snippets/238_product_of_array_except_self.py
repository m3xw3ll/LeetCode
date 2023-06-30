def product_except_self(nums):
        l = [1] * (len(nums))
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            l[i] = prefix
            prefix *= nums[i]
        for j in range(len(nums) - 1, -1, -1):
            l[j] *= postfix
            postfix *= nums[j]
        return l


print(product_except_self([1, 2, 3, 4]))
