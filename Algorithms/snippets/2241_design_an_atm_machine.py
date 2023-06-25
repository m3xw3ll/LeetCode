class ATM:
    def __init__(self):
        self.banknotes = {
            20: 0,
            50: 0,
            100: 0,
            200: 0,
            500: 0
        }

    def deposit(self, banknotes_count):
        for idx, banknote in [(0, 20), (1, 50), (2, 100), (3, 200), (4, 500)]:
            self.banknotes[banknote] += banknotes_count[idx]

    def withdraw(self, amount):
        out = [0, 0, 0, 0, 0]
        for idx, banknote in [(0, 500), (1, 200), (2, 100), (3, 50), (4, 20)]:
            if amount >= banknote:
                out[4 - idx] = (min(self.banknotes[banknote], amount // banknote))
                amount -= out[4 - idx] * banknote

        if amount:
            return [-1]

        for idx, banknote in [(0, 20), (1, 50), (2, 100), (3, 200), (4, 500)]:
            self.banknotes[banknote] -= out[idx]

        return out


if __name__ == '__main__':
    atm = ATM()
    atm.deposit([0, 0, 1, 2, 1])
    print(atm.withdraw(600))
    atm.deposit([0, 1, 0, 1, 1])
    print(atm.withdraw(600))
    print(atm.withdraw(550))
