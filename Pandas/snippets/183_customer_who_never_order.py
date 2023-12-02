import pandas as pd


def find_customers(customer, orders):
    data = pd.merge(customer, orders, left_on=['id'], right_on=['customerId'], how='outer')
    data = data[data['customerId'].isna()]
    return pd.DataFrame(data['name']).rename(columns={'name': 'Customers'})


if __name__ == '__main__':
    data = [[1, 'Joe'], [2, 'Henry'], [3, 'Sam'], [4, 'Max']]
    customers = pd.DataFrame(data, columns=['id', 'name']).astype({'id': 'Int64', 'name': 'object'})
    data = [[1, 3], [2, 1]]
    orders = pd.DataFrame(data, columns=['id', 'customerId']).astype({'id': 'Int64', 'customerId': 'Int64'})
    print(find_customers(customers, orders))