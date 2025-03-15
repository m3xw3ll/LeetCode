# [Product Sales Analysis III](https://leetcode.com/problems/product-sales-analysis-iii/description/)

Table: Sales
```
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.
``` 

Table: Product
```
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.
``` 

Write a solution to select the product id, year, quantity, and price for the first year of every product sold.

Return the resulting table in any order.

The result format is in the following example.

Example 1:
```
Input: 
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
Output: 
+------------+------------+----------+-------+
| product_id | first_year | quantity | price |
+------------+------------+----------+-------+ 
| 100        | 2008       | 10       | 5000  |
| 200        | 2011       | 15       | 9000  |
+------------+------------+----------+-------+
```
Solution
```python
import pandas as pd


def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    data = pd.merge(sales, product, how='right', on='product_id')
    data['first_year'] = data.groupby('product_id')['year'].transform('min')
    data = data[data['year'] == data['first_year']]
    return data[['product_id', 'first_year', 'quantity', 'price']]


if __name__ == '__main__':
    data = [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]]
    sales = pd.DataFrame(data, columns=['sale_id', 'product_id', 'year', 'quantity', 'price']).astype(
        {'sale_id': 'Int64', 'product_id': 'Int64', 'year': 'Int64', 'quantity': 'Int64', 'price': 'Int64'})
    data = [[100, 'Nokia'], [200, 'Apple'], [300, 'Samsung']]
    product = pd.DataFrame(data, columns=['product_id', 'product_name']).astype(
        {'product_id': 'Int64', 'product_name': 'object'})
    print(sales_analysis(sales, product))
```