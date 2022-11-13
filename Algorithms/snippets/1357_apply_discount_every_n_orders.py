class Cashier:
    def __init__(self, n, discount, products, prices):
        self.n = n
        self.discount = discount
        self.prices = dict()
        self.counter = 0
        for i in range(len(products)):
            self.prices[products[i]] = prices[i]

    def get_bill(self, product, amount):
        self.counter += 1
        bill = 0
        for i in range(len(product)):
            bill += self.prices[product[i]] * amount[i]

        if self.counter % self.n == 0:
            return bill * ((100 - self.discount) / 100)
        return bill


if __name__ == '__main__':
    c = Cashier(3, 50, [1, 2, 3, 4, 5, 6, 7], [100, 200, 300, 400, 300, 200, 100])
    print(c.get_bill([1, 2], [1, 2]))
    print(c.get_bill([3, 7], [10, 10]))
    print(c.get_bill([1, 2, 3, 4, 5, 6, 7], [1, 1, 1, 1, 1, 1, 1]))
    print(c.get_bill([4], [10]))
    print(c.get_bill([7, 3], [10, 10]))
    print(c.get_bill([7, 5, 3, 1, 6, 4, 2], [10, 10, 10, 9, 9, 9, 7]))
    print(c.get_bill([2, 3, 5], [5, 3, 2]))
