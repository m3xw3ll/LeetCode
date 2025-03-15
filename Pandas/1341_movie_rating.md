# [Movie Rating](https://leetcode.com/problems/movie-rating/description/)

Table: Movies
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| title         | varchar |
+---------------+---------+
movie_id is the primary key (column with unique values) for this table.
title is the name of the movie.
``` 

Table: Users
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| name          | varchar |
+---------------+---------+
user_id is the primary key (column with unique values) for this table.
``` 

Table: MovieRating
```
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| movie_id      | int     |
| user_id       | int     |
| rating        | int     |
| created_at    | date    |
+---------------+---------+
(movie_id, user_id) is the primary key (column with unique values) for this table.
This table contains the rating of a movie by a user in their review.
created_at is the user's review date. 
``` 

Write a solution to:

- Find the name of the user who has rated the greatest number of movies. In case of a tie, return the lexicographically smaller user name.
- Find the movie name with the highest average rating in February 2020. In case of a tie, return the lexicographically smaller movie name.

- The result format is in the following example.

Example 1:
```
Input: 
Movies table:
+-------------+--------------+
| movie_id    |  title       |
+-------------+--------------+
| 1           | Avengers     |
| 2           | Frozen 2     |
| 3           | Joker        |
+-------------+--------------+
Users table:
+-------------+--------------+
| user_id     |  name        |
+-------------+--------------+
| 1           | Daniel       |
| 2           | Monica       |
| 3           | Maria        |
| 4           | James        |
+-------------+--------------+
MovieRating table:
+-------------+--------------+--------------+-------------+
| movie_id    | user_id      | rating       | created_at  |
+-------------+--------------+--------------+-------------+
| 1           | 1            | 3            | 2020-01-12  |
| 1           | 2            | 4            | 2020-02-11  |
| 1           | 3            | 2            | 2020-02-12  |
| 1           | 4            | 1            | 2020-01-01  |
| 2           | 1            | 5            | 2020-02-17  | 
| 2           | 2            | 2            | 2020-02-01  | 
| 2           | 3            | 2            | 2020-03-01  |
| 3           | 1            | 3            | 2020-02-22  | 
| 3           | 2            | 4            | 2020-02-25  | 
+-------------+--------------+--------------+-------------+
Output: 
+--------------+
| results      |
+--------------+
| Daniel       |
| Frozen 2     |
+--------------+
Explanation: 
Daniel and Monica have rated 3 movies ("Avengers", "Frozen 2" and "Joker") but Daniel is smaller lexicographically.
Frozen 2 and Joker have a rating average of 3.5 in February but Frozen 2 is smaller lexicographically.
```
Solution
```python
import pandas as pd


def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    tmp = pd.merge(movie_rating, users, how='left', on='user_id')
    most_ratings = tmp.groupby('name')['user_id'].count().reset_index(name='cnt')
    most_ratings = most_ratings.sort_values(by=['cnt', 'name'], ascending=[False, True])['name'].iloc[0]

    tmp = pd.merge(movie_rating, movies, how='left', on='movie_id')
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
```