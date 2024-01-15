import pandas as pd


def users_percentage(users, register):
    tmp = register.groupby('contest_id')['user_id'].count().reset_index()
    user_cnt = users.shape[0]
    tmp['percentage'] = (100 / user_cnt * tmp['user_id']).round(2)
    tmp['percentage'] = tmp['percentage'].round(2)
    return tmp[['contest_id', 'percentage']].sort_values(by=['percentage', 'contest_id'], ascending=[False, True])


if __name__ == '__main__':
    data = [[6, 'Alice'], [2, 'Bob'], [7, 'Alex']]
    users = pd.DataFrame(data, columns=['user_id', 'user_name']).astype({'user_id': 'Int64', 'user_name': 'object'})
    data = [[215, 6], [209, 2], [208, 2], [210, 6], [208, 6], [209, 7], [209, 6], [215, 7], [208, 7], [210, 2],
            [207, 2], [210, 7]]
    register = pd.DataFrame(data, columns=['contest_id', 'user_id']).astype({'contest_id': 'Int64', 'user_id': 'Int64'})
    print(users_percentage(users, register))