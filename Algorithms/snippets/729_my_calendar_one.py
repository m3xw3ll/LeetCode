class MyCalendar:
    def __init__(self):
        self.meetings = []

    def book(self, start, end):
        for s, e in self.meetings:
            if s < end and start < e:
                return False
        self.meetings.append((start, end))
        return True


if __name__ == '__main__':
    cal = MyCalendar()
    print(cal.book(10, 20))
    print(cal.book(15, 25))
    print(cal.book(20, 30))