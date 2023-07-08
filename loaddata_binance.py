import pandas as pd
import os
import warnings

def readcsv(period, pair, duration):

    data = pd.DataFrame()

    current_dir = current_dir = os.path.dirname(os.path.abspath(__file__))

    start_date, end_date = duration.split(':')

    start_year, start_month, start_day = start_date.split('-')
    end_year, end_month, end_day = end_date.split('-')

    for year in range(int(start_year), int(end_year) + 1):

        start_month_val = int(start_month) if year == int(start_year) else 1
        end_month_val = int(end_month) if year == int(end_year) else 12

        for month in range(start_month_val, end_month_val + 1):
            
            try:
                temp = pd.read_csv(
                    current_dir + "\\binance_data\\{}\\{}\\{}-{}-{}-{:02d}.csv".format(pair, period, pair, period, year, month))
            except:
                warnings.warn("Cannot read partial data")
            temp.columns = ['Open_time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close_time', 'Base_asset_volume',
                                'Number_of_trades', 'Taker_buy_volume', 'Taker_buy_base_asset_volume', 'Ignore']
            temp['Open_time'] = pd.to_datetime(temp['Open_time'], unit='ms')
            temp.set_index("Open_time", inplace=True)
            data = pd.concat([data, temp])

    start_date = pd.to_datetime('{}-{}-{}'.format(start_year, start_month, start_day))
    end_date = pd.to_datetime('{}-{}-{}'.format(end_year, end_month, end_day))
    data = data[(data.index >= start_date) & (data.index <= end_date)]

    return data

#format
#data = readcsv('15m', 'BTCUSDT', '2023-04-01:2023-05-05')
#print(data)
