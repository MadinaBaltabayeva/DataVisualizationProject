import csv
from datetime import datetime
from matplotlib import pyplot as plt 

filename = 'data/sitka_weather_2018_simple2.csv'
with open (filename) as f: 
    reader = csv.reader(f)
    header_row = next(reader)
    # Чтение дат и максимальных температур из файла.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")  
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    print(highs)

# Нанесение данных на диаграмму.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1 ) 

# facecolor определяет цвет закрашиваемой области

# [ alpha ] oпределяет степень прозрачности вывода. Значение 0 означает полную прозрачность, 
# а 1 (по умолчанию) — полную непрозрачность. Со значением alpha=0.5 красные и синие линии 
# на графике становятся более светлыми.

# Форматирование диаграммы.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate() # выводит метки дат по диагонали, чтобы они не перекрывались.
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()