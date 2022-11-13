from sortedcontainers import SortedList


class MedianFinder:
    def __init__(self):
        self.arr = SortedList([])

    def add_number(self, num):
        self.arr.add(num)

    def find_median(self):
        l = len(self.arr)
        if l % 2 == 0:
            return (self.arr[l//2] + self.arr[l//2-1]) / 2
        else:
            return self.arr[l//2]


if __name__ == '__main__':
    m = MedianFinder()
    m.add_number(1)
    m.add_number(2)
    print(m.find_median())
    m.add_number(3)
    print(m.find_median())