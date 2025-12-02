import pandas as pd

# Load your weather CSV file
df = pd.read_csv("DailyDelhiClimateTest.csv")   # change file name to your dataset

# Show first 5 rows
print(df.head())

# Show basic info
print(df.info())

# Show summary statistics
print(df.describe())

# Handling missing values (choose one)
df = df.dropna()                     
# df = df.fillna(method='ffill')    

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['date'])

# Filter important columns (example)
df = df[['Date', 'meantemp', 'humidity', 'wind_speed', 'meanpressure']]
print(df.head())

import numpy as np

# Daily stats (already in df)
daily_mean = np.mean(df['meantemp'])
daily_min  = np.min(df['meantemp'])
daily_max  = np.max(df['meantemp'])
daily_std  = np.std(df['meantemp'])

print("Daily Temperature Mean:", daily_mean)
print("Daily Temperature Min:", daily_min)
print("Daily Temperature Max:", daily_max)
print("Daily Temperature Std Dev:", daily_std)

# Monthly and Yearly stats
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year

monthly_stats = df.groupby('Month')['meantemp'].mean()
yearly_stats = df.groupby('Year')['meantemp'].mean()

print(monthly_stats)
print(yearly_stats)


import matplotlib.pyplot as plt

# Line chart – daily temperature
plt.figure()
plt.plot(df['Date'], df['meantemp'])
plt.title("Daily Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature")
plt.savefig("daily_temperature.png")
plt.show()

# Bar chart – monthly rainfall
monthly_rainfall = df.groupby('Month')['Rainfall'].sum()

plt.figure()
plt.bar(monthly_rainfall.index, monthly_rainfall.values)
plt.title("Monthly Rainfall")
plt.xlabel("Month")
plt.ylabel("Rainfall (mm)")
plt.savefig("monthly_rainfall.png")
plt.show()

# Scatter plot – humidity vs temperature
plt.figure()
plt.scatter(df['Temperature'], df['Humidity'])
plt.title("Humidity vs Temperature")
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.savefig("humidity_vs_temperature.png")
plt.show()

# Combined Plot
plt.figure(figsize=(8,5))
plt.plot(df['Date'], df['meantemp'], label='Temperature')
plt.plot(df['Date'], df['humidity'], label='Humidity')
plt.legend()
plt.title("Temperature & Humidity Combined")
plt.savefig("combined_plot.png")
plt.show()

# Group by month
month_group = df.groupby('Month').mean()
print(month_group)

# Group by season (example)
def get_season(month):
    if month in [12, 1, 2]:
        return "Winter"
    elif month in [3, 4, 5]:
        return "Summer"
    elif month in [6, 7, 8]:
        return "Monsoon"
    else:
        return "Autumn"

df['Season'] = df['Month'].apply(get_season)

season_group = df.groupby('Season').mean()
print(season_group)


# Export cleaned CSV
df.to_csv("cleaned_weather_data.csv", index=False)

# Create a simple text summary report
report = """
Weather Data Insights Report
----------------------------

1. Average Temperature: {:.2f}
2. Minimum Temperature: {:.2f}
3. Maximum Temperature: {:.2f}

Monthly Rainfall Summary:
{}

Thank you!
""".format(daily_mean, daily_min, daily_max, monthly_rainfall.to_string())

with open("summary_report.txt", "w") as f:
    f.write(report)

print("Report, cleaned CSV, and images saved successfully!")

