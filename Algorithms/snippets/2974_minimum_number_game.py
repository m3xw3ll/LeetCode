import heapq


def number_game(nums):
    out = []
    heapq.heapify(nums)

    while len(nums) > 0:
        num_alice = heapq.heappop(nums)
        num_bob = heapq.heappop(nums)
        out.append(num_bob)
        out.append(num_alice)
    return out


print(number_game([5,4,2,3]))