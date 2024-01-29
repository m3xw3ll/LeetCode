import pandas as pd


def queries_stats(queries):
    queries['quality'] = queries['rating'] / queries['position']
    queries['poor_query_percentage'] = (queries['rating'] < 3) * 100
    out = queries.groupby(['query_name']).agg({'quality': 'mean',
                                               'poor_query_percentage':  'mean'}).round(2).reset_index()
    return out


if __name__ == '__main__':
    data = [['Dog', 'Golden Retriever', 1, 5], ['Dog', 'German Shepherd', 2, 5], ['Dog', 'Mule', 200, 1],
            ['Cat', 'Shirazi', 5, 2], ['Cat', 'Siamese', 3, 3], ['Cat', 'Sphynx', 7, 4]]
    queries = pd.DataFrame(data, columns=['query_name', 'result', 'position', 'rating']).astype(
        {'query_name': 'object', 'result': 'object', 'position': 'Int64', 'rating': 'Int64'})
    print(queries_stats(queries))