# [Monthly Transactions I](https://leetcode.com/problems/monthly-transactions-i/description/)

Table: Transactions
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| country       | varchar |
| state         | enum    |
| amount        | int     |
| trans_date    | date    |
+---------------+---------+
id is the primary key of this table.
The table has information about incoming transactions.
The state column is an enum of type ["approved", "declined"].
``` 

Write an SQL query to find for each month and country, the number of transactions and their total amount, the number of
approved transactions and their total amount.

Return the result table in any order.

The query result format is in the following example.

Example 1:
```
Input: 
Transactions table:
+------+---------+----------+--------+------------+
| id   | country | state    | amount | trans_date |
+------+---------+----------+--------+------------+
| 121  | US      | approved | 1000   | 2018-12-18 |
| 122  | US      | declined | 2000   | 2018-12-19 |
| 123  | US      | approved | 2000   | 2019-01-01 |
| 124  | DE      | approved | 2000   | 2019-01-07 |
+------+---------+----------+--------+------------+
Output: 
+----------+---------+-------------+----------------+--------------------+-----------------------+
| month    | country | trans_count | approved_count | trans_total_amount | approved_total_amount |
+----------+---------+-------------+----------------+--------------------+-----------------------+
| 2018-12  | US      | 2           | 1              | 3000               | 1000                  |
| 2019-01  | US      | 1           | 1              | 2000               | 2000                  |
| 2019-01  | DE      | 1           | 1              | 2000               | 2000                  |
+----------+---------+-------------+----------------+--------------------+-----------------------+
```
Solution
```python
import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['trans_date'] = transactions['trans_date'].dt.strftime('%Y-%m')
    transactions['approved'] = np.where(transactions['state'] == 'approved', 1, 0)
    transactions['approved_amount'] = np.where(transactions['state'] == 'approved', transactions['amount'], 0)
    out = transactions.groupby(['country', 'trans_date'], dropna=False).agg({
        'state': 'count',
        'approved': 'sum',
        'approved_amount': 'sum',
        'amount': 'sum'
    }).reset_index()
    out.columns = ['country', 'month', 'trans_count', 'approved_count', 'approved_total_amount', 'trans_total_amount']
    return out[['month', 'country', 'trans_count', 'approved_count', 'trans_total_amount', 'approved_total_amount']]


if __name__ == '__main__':
    data = [[121, 'US', 'approved', 1000, '2018-12-18'], [122, 'US', 'declined', 2000, '2018-12-19'],
            [123, 'US', 'approved', 2000, '2019-01-01'], [124, 'DE', 'approved', 2000, '2019-01-07']]
    transactions = pd.DataFrame(data, columns=['id', 'country', 'state', 'amount', 'trans_date']).astype(
        {'id': 'Int64', 'country': 'object', 'state': 'object', 'amount': 'Int64', 'trans_date': 'datetime64[ns]'})
    print(monthly_transactions(transactions))
```