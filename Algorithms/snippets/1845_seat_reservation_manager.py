import heapq


class SeatManager:
    def __init__(self, n):
        self.heap = [x for x in range(1, n + 1)]

    def reserve(self):
        return heapq.heappop(self.heap)

    def unreserve(self, seat_number):
        heapq.heappush(self.heap, seat_number)


if __name__ == '__main__':
    s = SeatManager(5)
    print(s.reserve())
    print(s.reserve())
    print(s.unreserve(2))
    print(s.reserve())
    print(s.reserve())
    print(s.reserve())
    print(s.unreserve(5))