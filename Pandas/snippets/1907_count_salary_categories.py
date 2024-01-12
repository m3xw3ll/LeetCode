import pandas as pd


def count_salary_categories(accounts):
    types = ['Low Salary', 'Average Salary', 'High Salary']
    low = len(accounts[accounts['income'] < 20000])
    high = len(accounts[accounts['income'] > 50000])
    avg = len(accounts) - low - high
    return pd.DataFrame({'category': types, 'accounts_count': [low, avg, high]})


if __name__ == '__main__':
    data = [[3, 108939], [2, 12747], [8, 87709], [6, 91796]]
    accounts = pd.DataFrame(data, columns=['account_id', 'income']).astype({'account_id': 'Int64', 'income': 'Int64'})
    print(count_salary_categories(accounts))