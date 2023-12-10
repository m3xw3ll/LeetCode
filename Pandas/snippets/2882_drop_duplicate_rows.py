import pandas as pd


def drop_duplicate_emails(customers):
    return customers.drop_duplicates(subset='email', keep='first')


if __name__ == '__main__':
    data = [[1, 'Ella', 'emily@example.com'],
            [2, 'David', 'michael@example.com'],
            [3, 'Zachary', 'sarah@example.com'],
            [4, 'Alice', 'john@example.com'],
            [5, 'Finn', 'john@example.com'],
            [6, 'Violet', 'alice@example.com']]
    customers = pd.DataFrame(data, columns=['customer_id', 'name', 'email'])
    print(drop_duplicate_emails(customers))