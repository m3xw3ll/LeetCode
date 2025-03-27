def find_peaks(mountain):
    peaks = []
    for i in range(1, len(mountain) - 1):
        if mountain[i - 1] < mountain[i] > mountain[i+1]:
            peaks.append(i)
    return peaks


print(find_peaks([1, 4, 3, 8, 5]))
