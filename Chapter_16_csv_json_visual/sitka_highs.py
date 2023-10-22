import csv

filename = 'sitka_weather_2021_simple.csv'
with open(filename) as file:
    reader = csv.reader(file)
    header_now = next(reader)

    for index, column_header in enumerate(header_now):
        print(index, column_header)