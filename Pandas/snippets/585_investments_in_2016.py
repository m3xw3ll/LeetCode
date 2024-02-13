import pandas as pd


def find_investments(insurance):
    insurance['count2015'] = insurance.groupby('tiv_2015')['pid'].transform('count')
    insurance['latlon'] = insurance.groupby(['lat','lon'])['pid'].transform('count')
    insurance = insurance[(insurance['count2015']>1) & (insurance['latlon']==1)][['tiv_2016']].sum().to_frame('tiv_2016').round(2)
    return insurance


if __name__ == '__main__':
    data = [[1, 10, 5, 10, 10], [2, 20, 20, 20, 20], [3, 10, 30, 20, 20], [4, 10, 40, 40, 40]]
    insurance = pd.DataFrame(data, columns=['pid', 'tiv_2015', 'tiv_2016', 'lat', 'lon']).astype(
        {'pid': 'Int64', 'tiv_2015': 'Float64', 'tiv_2016': 'Float64', 'lat': 'Float64', 'lon': 'Float64'})
    print(find_investments(insurance))