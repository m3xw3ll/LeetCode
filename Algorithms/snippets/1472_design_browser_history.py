class BrowserHistory:
    def __init__(self, homepage):
        self.homepages = [homepage]
        self.fw = []

    def visit(self, url):
        self.homepages.append(url)
        self.fw = []

    def back(self, steps):
        while len(self.homepages) > 1 and steps:
            tmp_url = self.homepages.pop()
            steps -= 1
            self.fw.append(tmp_url)
        return self.homepages[-1]

    def forward(self, steps):
        if not self.fw:
            return self.homepages[-1]
        while len(self.fw) >= 1 and steps:
            tmp_url = self.fw.pop()
            steps -= 1
            self.homepages.append(tmp_url)
        return self.homepages[-1]


if __name__ == '__main__':
    bh = BrowserHistory('leetcode.com')
    bh.visit('google.com')
    bh.visit('facebook.com')
    bh.visit('youtube.de')
    print(bh.back(1))
    print(bh.back(1))
    print(bh.forward(1))
    bh.visit('linkedin.com')
    print(bh.forward(2))
    print(bh.back(2))
    print(bh.back(7))