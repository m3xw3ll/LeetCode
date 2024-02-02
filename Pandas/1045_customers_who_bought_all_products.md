# [Customers Who Bought All Products](https://leetcode.com/problems/customers-who-bought-all-products/description/)

Table: Customer
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
This table may contain duplicates rows. 
customer_id is not NULL.
product_key is a foreign key (reference column) to Product table.
``` 

Table: Product
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
product_key is the primary key (column with unique values) for this table.
``` 

Write a solution to report the customer ids from the Customer table that bought all the products in the Product table.

Return the result table in any order.

The result format is in the following example.

Example 1:
```
Input: 
Customer table:
+-------------+-------------+
| customer_id | product_key |
+-------------+-------------+
| 1           | 5           |
| 2           | 6           |
| 3           | 5           |
| 3           | 6           |
| 1           | 6           |
+-------------+-------------+
Product table:
+-------------+
| product_key |
+-------------+
| 5           |
| 6           |
+-------------+
Output: 
+-------------+
| customer_id |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation: 
The customers who bought all the products (5 and 6) are customers with IDs 1 and 3.
```
Solution
```python
import pandas as pd


def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    out = customer.drop_duplicates(keep='first').groupby(['customer_id'])['product_key'].count().reset_index(name='cnt')
    return out[out['cnt'] >= product.shape[0]][['customer_id']]


if __name__ == '__main__':
    data = [[18, 15], [40, 9], [35, 17], [25, 16], [12, 11], [35, 7]]
    customer = pd.DataFrame(data, columns=['customer_id', 'product_key']).astype(
        {'customer_id': 'Int64', 'product_key': 'Int64'})
    data = [[15], [1], [20], [14], [18], [8]]
    product = pd.DataFrame(data, columns=['product_key']).astype({'product_key': 'Int64'})
    print(find_customers(customer, product))
```