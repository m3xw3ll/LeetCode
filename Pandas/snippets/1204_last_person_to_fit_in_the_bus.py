import pandas as pd


def last_passenger(queue):
    queue = queue.sort_values(by='turn')
    queue['cumweight'] = queue['weight'].cumsum()
    return queue[queue['cumweight'] <= 1000]['person_name'].tail(1)


if __name__ == '__main__':
    data = [[5, 'Alice', 250, 1], [4, 'Bob', 175, 5], [3, 'Alex', 350, 2], [6, 'John Cena', 400, 3],
            [1, 'Winston', 500, 6], [2, 'Marie', 200, 4]]
    queue = pd.DataFrame(data, columns=['person_id', 'person_name', 'weight', 'turn']).astype(
        {'person_id': 'Int64', 'person_name': 'object', 'weight': 'Int64', 'turn': 'Int64'})
    print(last_passenger(queue))