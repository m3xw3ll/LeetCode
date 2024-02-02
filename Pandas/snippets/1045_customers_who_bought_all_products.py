import pandas as pd


def find_customers(customer, product):
    out = customer.drop_duplicates(keep='first').groupby(['customer_id'])['product_key'].count().reset_index(name='cnt')
    out = out[out['cnt'] >= product.shape[0]]
    return out['customer_id']


if __name__ == '__main__':
    data = [[18, 15], [40, 9], [35, 17], [25, 16], [12, 11], [35, 7]]
    customer = pd.DataFrame(data, columns=['customer_id', 'product_key']).astype(
        {'customer_id': 'Int64', 'product_key': 'Int64'})
    data = [[15], [1], [20], [14], [18], [8]]
    product = pd.DataFrame(data, columns=['product_key']).astype({'product_key': 'Int64'})
    print(find_customers(customer, product))