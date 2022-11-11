class Bank:
    def __init__(self, balance):
        self.accounts = balance

    def transfer(self, account1, account2, money):
        if self.check_account(account1) and self.check_account(account2) and self.accounts[account1-1] >= money:
            self.accounts[account1-1] -= money
            self.accounts[account2-1] += money
            return True

    def deposit(self, account, money):
        if self.check_account(account):
            self.accounts[account-1] += money
            return True

    def withdraw(self, account, money):
        if self.check_account(account) and self.accounts[account-1] >= money:
            self.accounts[account-1] -= money
            return True

    def check_account(self, account):
        if 1 <= account <= len(self.accounts):
            return True


if __name__ == '__main__':
    bank = Bank([10, 100, 20, 50, 30])
    print(bank.withdraw(3, 10))
    print(bank.transfer(5, 1, 10))
    print(bank.deposit(5, 20))
    print(bank.transfer(3, 4, 15))
    print(bank.withdraw(10, 50))