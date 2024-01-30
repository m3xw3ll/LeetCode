import pandas as pd


def sales_analysis(sales, product):
    data = pd.merge(sales, product, how='right', on='product_id')
    data['first_year'] = data.groupby('product_id')['year'].transform('min')
    data = data[data['year'] == data['min_year']]
    return data[['product_id', 'first_year', 'quantity', 'price']]


if __name__ == '__main__':
    data = [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]]
    sales = pd.DataFrame(data, columns=['sale_id', 'product_id', 'year', 'quantity', 'price']).astype(
        {'sale_id': 'Int64', 'product_id': 'Int64', 'year': 'Int64', 'quantity': 'Int64', 'price': 'Int64'})
    data = [[100, 'Nokia'], [200, 'Apple'], [300, 'Samsung']]
    product = pd.DataFrame(data, columns=['product_id', 'product_name']).astype(
        {'product_id': 'Int64', 'product_name': 'object'})
    print(sales_analysis(sales, product))