import pandas as pd


def restaurant_growth(customer):
    customer = customer.sort_values(by=['visited_on'])
    customer = customer.groupby('visited_on')['amount'].sum().reset_index()
    customer['average_amount'] = customer['amount'].rolling(window=7).mean().round(2)
    customer['amount'] = customer['amount'].rolling(window=7).sum().round(2)
    return customer[['visited_on', 'amount', 'average_amount']].dropna()


if __name__ == '__main__':
    data = [[1, 'Jhon', '2019-01-01', 100], [2, 'Daniel', '2019-01-02', 110], [3, 'Jade', '2019-01-03', 120],
            [4, 'Khaled', '2019-01-04', 130], [5, 'Winston', '2019-01-05', 110], [6, 'Elvis', '2019-01-06', 140],
            [7, 'Anna', '2019-01-07', 150], [8, 'Maria', '2019-01-08', 80], [9, 'Jaze', '2019-01-09', 110],
            [1, 'Jhon', '2019-01-10', 130], [3, 'Jade', '2019-01-10', 150]]
    customer = pd.DataFrame(data, columns=['customer_id', 'name', 'visited_on', 'amount']).astype(
        {'customer_id': 'Int64', 'name': 'object', 'visited_on': 'datetime64[ns]', 'amount': 'Int64'})
    print(restaurant_growth(customer))