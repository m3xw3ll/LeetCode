import pandas as pd


def get_dataframe_size(players):
    return list(players.shape)


if __name__ == '__main__':
    data = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            ]
    players = pd.DataFrame(data, columns=['Col1', 'Col2', 'Col3', 'Col4', 'Col5'])
    print(get_dataframe_size(players))
