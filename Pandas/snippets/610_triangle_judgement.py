import pandas as pd


def check_sides(row):
    sorted_row = sorted(row)
    smallest = sorted_row[0]
    second_smallest = sorted_row[1]
    third_smallest = sorted_row[2]
    return "Yes" if smallest + second_smallest > third_smallest else "No"


def triangle_judgement(triangle):
    triangle['triangle'] = triangle.apply(check_sides, axis=1)
    return triangle


if __name__ == '__main__':
    data = [[13, 15, 30], [10, 20, 15]]
    triangle = pd.DataFrame(data, columns=['x', 'y', 'z']).astype({'x': 'Int64', 'y': 'Int64', 'z': 'Int64'})
    print(triangle_judgement(triangle))