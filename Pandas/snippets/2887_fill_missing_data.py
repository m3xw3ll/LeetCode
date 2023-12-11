import pandas as pd


def fill_missing_values(products):
    products['quantity'].fillna(0, inplace=True)
    return products


if __name__ == '__main__':
    data = [['Wristwatch', None, 135],
            ['WirelessEarbuds', None, 821],
            ['GolfClubs', 779, 9319],
            ['Printer', 849, 3051]]
    products = pd.DataFrame(data, columns=['name', 'quantity', 'price'])
    print(fill_missing_values(products))