import pandas as pd


def movie_rating(movies, users, movie_ratings):
    tmp = pd.merge(movie_ratings, users, how='left', on='user_id')
    most_ratings = tmp.groupby('name')['user_id'].count().reset_index(name='cnt')
    most_ratings = most_ratings.sort_values(by=['cnt', 'name'], ascending=[False, True])['name'].iloc[0]

    tmp = pd.merge(movie_ratings, movies, how='left', on='movie_id')
    tmp['created_at'] = pd.to_datetime(tmp['created_at'])
    tmp = tmp[(tmp['created_at'].dt.year == 2020) & (tmp['created_at'].dt.month == 2)]
    highest_rating = tmp.groupby('title')['rating'].mean().reset_index(name='avg')
    highest_rating = highest_rating.sort_values(by=['avg', 'title'], ascending=[False, True])['title'].iloc[0]
    return pd.DataFrame([[most_ratings], [highest_rating]], columns=['results'])


if __name__ == '__main__':
    data = [[1, 'Avengers'], [2, 'Frozen 2'], [3, 'Joker']]
    movies = pd.DataFrame(data, columns=['movie_id', 'title']).astype({'movie_id': 'Int64', 'title': 'object'})
    data = [[1, 'Daniel'], [2, 'Monica'], [3, 'Maria'], [4, 'James']]
    users = pd.DataFrame(data, columns=['user_id', 'name']).astype({'user_id': 'Int64', 'name': 'object'})
    data = [[1, 1, 3, '2020-01-12'], [1, 2, 4, '2020-02-11'], [1, 3, 2, '2020-02-12'], [1, 4, 1, '2020-01-01'],
            [2, 1, 5, '2020-02-17'], [2, 2, 2, '2020-02-01'], [2, 3, 2, '2020-03-01'], [3, 1, 3, '2020-02-22'],
            [3, 2, 4, '2020-02-25']]
    movie_ratings = pd.DataFrame(data, columns=['movie_id', 'user_id', 'rating', 'created_at']).astype(
        {'movie_id': 'Int64', 'user_id': 'Int64', 'rating': 'Int64', 'created_at': 'datetime64[ns]'})
    print(movie_rating(movies, users, movie_ratings))