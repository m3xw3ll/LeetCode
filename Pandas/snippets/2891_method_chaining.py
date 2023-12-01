import pandas as pd


def find_heavy_animals(animals):
    return pd.DataFrame(animals.loc[animals['weight'] > 100].sort_values(by=['weight'], ascending=False)['name'],
                        columns=['name'])


if __name__ == '__main__':
    data = {"headers": {"animals": ["name", "species", "age", "weight"]}, "rows": {
        "animals": [["Tatiana", "Snake", 98, 464], ["Khaled", "Giraffe", 50, 41], ["Alex", "Leopard", 6, 328],
                    ["Jonathan", "Monkey", 45, 463], ["Stefan", "Bear", 100, 50], ["Tommy", "Panda", 26, 349]]}}
    animals = pd.DataFrame(data['rows']['animals'], columns=data['headers']['animals'])
    print(find_heavy_animals(animals))