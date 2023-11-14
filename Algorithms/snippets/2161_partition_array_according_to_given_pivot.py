def pivot_array(nums, pivot):
    smaller = []
    greater = []
    eq = 0

    for n in nums:
        if n < pivot:
            smaller.append(n)
        elif n > pivot:
            greater.append(n)
        else:
            eq += 1
    return smaller + [pivot] * eq + greater


print(pivot_array(nums=[9, 12, 5, 10, 14, 3, 10], pivot=10))
