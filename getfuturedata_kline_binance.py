import os
import json
import datetime
#================================================================
pairs = ["BNBUSDT","BTCUSDT","ETHUSDT",]
interval_ = ['1h','15m','1D','1W','4h']


#================================================================
current_date = datetime.date.today()
to_month = current_date.month-1
to_year = current_date.year

downloaded_data = []
if os.path.exists("downloaded_data.json"):
    with open("downloaded_data.json", "r") as file:
        downloaded_data = json.load(file)

for pair in pairs:
    for interval in interval_:
        try:
            os.makedirs(os.path.join("binance_data", pair, interval))
        except:
            pass

        for year in range(2023, 2019, -1):
            end_month = 12 if year != to_year else to_month  # Download until May 2023

            for month in range(1, end_month + 1):
                file_path = "binance_data/{}/{}/{}-{}-{}-{:02d}.zip".format(
                    pair, interval, pair, interval, year, month)

                # Check if the file already exists using JSON data
                if not any(data["pair"] == pair and data["year"] == year and data["month"] == month and data["interval"] == interval for data in downloaded_data):
                    download_status = os.system(
                        "curl https://data.binance.vision/data/futures/um/monthly/klines/{}/{}/{}-{}-{}-{:02d}.zip --output {}".format(
                            pair, interval, pair, interval, year, month, file_path))

                    if download_status == 0:
                        downloaded_data.append({
                            "pair": pair,
                            "year": year,
                            "month": month,
                            "interval": interval
                        })
                        print("Downloaded: {} {} {} {}".format(
                            pair, interval, year, month))
                    else:
                        print("Failed to download: {} {} {} {}".format(
                            pair, interval, year, month))

                    # Save the downloaded data to JSON file after each pair
with open("downloaded_data.json", "w") as file:
    json.dump(downloaded_data, file)
                #else:
                    #print("already exists")
# Print the downloaded data
for data in downloaded_data:
    print(data)





