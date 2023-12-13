import pandas as pd


def biggest_single_number(my_numbers):
    unq = my_numbers['num'].drop_duplicates(keep=False)
    return pd.DataFrame([max(unq, default=None)], columns=['num'])


if __name__ == '__main__':
    data = [[8], [8], [3], [3], [1], [4], [5], [6]]
    my_numbers = pd.DataFrame(data, columns=['num']).astype({'num': 'Int64'})
    print(biggest_single_number(my_numbers))