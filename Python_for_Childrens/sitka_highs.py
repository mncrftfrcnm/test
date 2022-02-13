from datetime import datetime
import csv
from matplotlib import pyplot as plt
first_date = datetime.strptime('2021-09-01', '%Y-%m-%d')
print(first_date)
filename = 'sitka_weather.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    highs, lows, dates = [], [], []
    for row in reader:
        try:
            dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
            lows.append(row[0])
            highs.append(row[4]) 
        except ValueError:
            print("We haven't enough information")
        else:
            pass
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
plt.title('Daily high and low temperatures 2021', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (f)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()