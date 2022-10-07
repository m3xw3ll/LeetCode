def sort_array(nums):
    if len(nums) > 1:
        r = len(nums)//2
        L = nums[:r]
        M = nums[r:]

        sort_array(L)
        sort_array(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                nums[k] = L[i]
                i += 1
            else:
                nums[k] = M[j]
                j += 1
            k += 1
        while i < len(L):
            nums[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            nums[k] = M[j]
            j += 1
            k += 1
    return nums


print(sort_array([5, 2, 3, 1]))
