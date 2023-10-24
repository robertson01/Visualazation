import csv
from matplotlib import pyplot as pt
from datetime import datetime

filename = "sitka_weather_2021_simple.csv"
with open(filename) as file:
    reader = csv.reader(file)
    header_row = next(reader)
    for index, colum_header in enumerate(header_row):
        print(index, colum_header)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        try:
            low = int(row[4])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            lows.append(low)
            dates.append(current_date)

# Нанесение данных на диаграмму
pt.style.use('seaborn-v0_8')
fig, ax = pt.subplots(figsize=(15, 9))
ax.plot(dates, lows, c='red')

# Форматирование диаграммы
pt.title("Daily precipitation - 2023", fontsize=24)
pt.xlabel('', fontsize=16)
fig.autofmt_xdate()
pt.ylabel("Temperature (F)", fontsize=16)
pt.tick_params(axis='both', which='major', labelsize=16)
pt.show()