from collections import defaultdict


def count_balls(low_limit, high_limit):
    boxes = defaultdict(int)
    for i in range(low_limit, high_limit + 1):
        ballsums = sum([int(x) for x in str(i)])
        boxes[ballsums] += 1
    return max(boxes.values())


print(count_balls(1, 10))