import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

API_KEY = 'YOUR_API_KEY_HERE'
CITY = 'Mumbai'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={'bangalore'}&appid={'efc73867c3bb81cefaca9d6f10f38c42'}&units=metric'

response = requests.get(URL)

if response.status_code != 200:
    print("Error fetching data:", response.json().get("message", "Unknown error"))
    exit()

data = response.json()

dates = []
temperatures = []
humidity = []

for entry in data['list']:
    dt_txt = entry['dt_txt']
    temp = entry['main']['temp']
    hum = entry['main']['humidity']

    dates.append(datetime.strptime(dt_txt, '%Y-%m-%d %H:%M:%S'))
    temperatures.append(temp)
    humidity.append(hum)

sns.set_theme(style="darkgrid")
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.lineplot(x=dates, y=temperatures, color='orange')
plt.title(f'Temperature Forecast for {'bangalore'}')
plt.xlabel('Date & Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)

plt.subplot(1, 2, 2)
date_labels = [date.strftime('%b %d') for date in dates[::8]]
sns.barplot(x=date_labels, y=humidity[::8], palette='Blues_d')
plt.title(f'Daily Humidity Forecast for {'bangalore'}')
plt.xlabel('Date')
plt.ylabel('Humidity (%)')

plt.tight_layout()
plt.savefig('weather_dashboard.png')
plt.show()
