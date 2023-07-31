def shift_grid(grid, k):
    cols = len(grid[0])
    flat = sum(grid, [])
    k = k % len(flat)
    flat = flat[-k:] + flat[:-k]
    return [flat[i:i + cols] for i in range(0, len(flat), cols)]


print(shift_grid(grid=[[1], [2], [3], [4], [7], [6], [5]], k=23))
