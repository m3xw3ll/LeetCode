import pandas as pd
import numpy as np


def immediate_food_delivery(delivery):
    delivery = delivery.sort_values(by=['customer_id', 'order_date'])
    delivery = delivery.drop_duplicates(subset='customer_id', keep='first')
    delivery['flag'] = np.where(delivery['order_date'] == delivery['customer_pref_delivery_date'], 1, 0)
    return pd.DataFrame([np.round(((delivery['flag'].sum() / len(delivery)) * 100), 2)], columns=['immediate_percentage'])


if __name__ == '__main__':
    data = [[1, 1, '2019-08-01', '2019-08-02'], [2, 2, '2019-08-02', '2019-08-02'], [3, 1, '2019-08-11', '2019-08-12'],
            [4, 3, '2019-08-24', '2019-08-24'], [5, 3, '2019-08-21', '2019-08-22'], [6, 2, '2019-08-11', '2019-08-13'],
            [7, 4, '2019-08-09', '2019-08-09']]
    delivery = pd.DataFrame(data,
                            columns=['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date']).astype(
        {'delivery_id': 'Int64', 'customer_id': 'Int64', 'order_date': 'datetime64[ns]',
         'customer_pref_delivery_date': 'datetime64[ns]'})
    print(immediate_food_delivery(delivery))