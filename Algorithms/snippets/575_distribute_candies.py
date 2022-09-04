def distribute_candies(candy_type):
    maxcandy = len(candy_type) // 2
    unique_candy = len(set(candy_type))
    if maxcandy < unique_candy:
        return maxcandy
    return unique_candy


print(distribute_candies([6, 6, 6, 6]))