def result_array(nums):
    arr1 = [nums[0]]
    arr2 = [nums[1]]
    for i in range(2, len(nums)):
        arr1.append(nums[i]) if arr1[-1] > arr2[-1] else arr2.append(nums[i])
    return arr1 + arr2

print(result_array([2,1,3]))