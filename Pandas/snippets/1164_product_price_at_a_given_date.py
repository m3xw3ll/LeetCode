import pandas as pd
from datetime import datetime


def price_at_given_date(products):
    filtered_df = products[products['change_date'] <= datetime(2019, 8, 16)].sort_values(by=['product_id', 'change_date'])
    last_price = filtered_df.groupby('product_id').last().reset_index()
    all_products = pd.DataFrame({'product_id': range(1, products['product_id'].max() + 1)})
    out = pd.merge(all_products, last_price, on='product_id', how='left').fillna(10)
    return out[['product_id', 'new_price']].rename(columns={'new_price': 'price'})


if __name__ == '__main__':
    data = [[1, 20, '2019-08-14'], [2, 50, '2019-08-14'], [1, 30, '2019-08-15'], [1, 35, '2019-08-16'],
            [2, 65, '2019-08-17'], [3, 20, '2019-08-18']]
    products = pd.DataFrame(data, columns=['product_id', 'new_price', 'change_date']).astype(
        {'product_id': 'Int64', 'new_price': 'Int64', 'change_date': 'datetime64[ns]'})
    print(price_at_given_date(products))