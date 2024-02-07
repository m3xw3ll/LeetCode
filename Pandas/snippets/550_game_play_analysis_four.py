import pandas as pd


def gameplay_analysis(activity):
    activity['first'] = activity.groupby('player_id')['event_date'].transform(min)
    active_sec_day = activity.loc[activity['first'] + pd.DateOffset(1) == activity['event_date']]
    return pd.DataFrame([round(len(active_sec_day) / activity.player_id.nunique(),2)], columns=['fraction'])


if __name__ == '__main__':
    data = [[1, 2, '2016-03-01', 5], [1, 2, '2016-03-02', 6], [2, 3, '2017-06-25', 1], [3, 1, '2016-03-02', 0],
            [3, 4, '2018-07-03', 5]]
    activity = pd.DataFrame(data, columns=['player_id', 'device_id', 'event_date', 'games_played']).astype(
        {'player_id': 'Int64', 'device_id': 'Int64', 'event_date': 'datetime64[ns]', 'games_played': 'Int64'})
    print(gameplay_analysis(activity))