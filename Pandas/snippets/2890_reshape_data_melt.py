import pandas as pd


def melt_table(report):
    return pd.melt(report, id_vars=['product'], var_name='quarter', value_name='sales')


if __name__ == '__main__':
    data = [['Umbrella', 417, 224, 379, 611],
            ['SleepingBag', 800, 936, 93, 875]]
    report = pd.DataFrame(data, columns=['product', 'quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'])
    print(melt_table(report))