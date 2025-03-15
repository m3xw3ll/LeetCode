import pandas as pd


def exchange_seats(seats):
    seat_no = list(range(1, len(seats) + 1))
    for i in range(1, len(seats), 2):
        seat_no[i], seat_no[i-1] = seat_no[i-1], seat_no[i]
    seats['id'] = seat_no
    return seat.sort_values('id')


if __name__ == '__main__':
    data = [[1, 'Abbot'], [2, 'Doris'], [3, 'Emerson'], [4, 'Green'], [5, 'Jeames']]
    seat = pd.DataFrame(data, columns=['id', 'student']).astype({'id': 'Int64', 'student': 'object'})
    print(exchange_seats(seat))