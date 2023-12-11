import pandas as pd


def pivot_table(weather):
    return weather.pivot(index='month', columns='city', values='temperature')


if __name__ == '__main__':
    data = [['Jacksonville', 'January', 13],
            ['Jacksonville', 'February', 23],
            ['Jacksonville', 'March', 38],
            ['Jacksonville', 'April', 5],
            ['Jacksonville', 'May', 34],
            ['ElPaso', 'January', 20],
            ['ElPaso', 'February', 6],
            ['ElPaso', 'March', 26],
            ['ElPaso', 'April', 2],
            ['ElPaso', 'May', 43]
            ]
    weather = pd.DataFrame(data, columns=['city', 'month', 'temperature'])
    print(pivot_table(weather))