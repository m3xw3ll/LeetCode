class RecentCounter:
    def __init__(self):
        self.cnt = []

    def ping(self, t):
        self.cnt.append(t)
        while self.cnt[0] < t - 3000:
            self.cnt.pop(0)
        return len(self.cnt)


if __name__ == '__main__':
    r = RecentCounter()
    print(r.ping(1))
    print(r.ping(100))
    print(r.ping(3001))
    print(r.ping(3002))