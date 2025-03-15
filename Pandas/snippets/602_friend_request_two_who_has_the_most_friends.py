import pandas as pd
from collections import Counter


def most_friends(request_accepted):
    lst = request_accepted['requester_id'].values.tolist() + request_accepted['accepter_id'].values.tolist()
    most_common = Counter(lst).most_common(1)
    out = pd.DataFrame([[most_common[0][0], most_common[0][1]]], columns=['id', 'num'])
    return out


if __name__ == '__main__':
    data = [[1, 2, '2016/06/03'], [1, 3, '2016/06/08'], [2, 3, '2016/06/08'], [3, 4, '2016/06/09']]
    request_accepted = pd.DataFrame(data, columns=['requester_id', 'accepter_id', 'accept_date']).astype(
        {'requester_id': 'Int64', 'accepter_id': 'Int64', 'accept_date': 'datetime64[ns]'})
    print(most_friends(request_accepted))