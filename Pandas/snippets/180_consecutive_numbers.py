import pandas as pd


def consecutive_numbers(logs):
    logs['tmp'] = logs['num'].rolling(window=3).var()
    nums = logs[logs['tmp'] == 0]['num'].unique().tolist()
    return pd.DataFrame(nums, columns=['ConsecutiveNums'])


if __name__ == '__main__':
    data = [[1, 1], [2, 1], [3, 1], [4, 2], [5, 1], [6, 2], [7, 2]]
    logs = pd.DataFrame(data, columns=['id', 'num']).astype({'id': 'Int64', 'num': 'Int64'})
    print(consecutive_numbers(logs))