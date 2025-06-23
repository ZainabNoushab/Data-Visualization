import pandas as pd
import matplotlib.pyplot as plt
import os

# Create 'figures' folder if it doesn't exist
if not os.path.exists("figures"):
    os.makedirs("figures")

# Loading the dataset
data = {
    "Date": pd.date_range(start="2025-06-09", periods=14, freq='D'),
    "Sleep_Hours": [7, 6.5, 8, 7.5, 7, 6, 6.5, 8, 7, 7.5, 6.5, 7, 8, 7],
    "Quran_Minutes": [10, 0, 15, 10, 20, 5, 10, 15, 0, 20, 10, 10, 25, 15],
    "Learning_Hours": [2, 4, 4.5, 3, 5, 5, 4, 3.5, 4, 6, 5, 4.5, 3, 2.5],
    "English_Minutes": [5, 10, 10, 0, 15, 10, 10, 5, 0, 15, 10, 10, 5, 5],
    "Mood_Rating": [7, 6, 8, 7, 9, 6, 7, 8, 6, 9, 8, 8, 7, 7],
    "Namaz_Offered": [5, 4, 5, 3, 5, 2, 4, 5, 3, 5, 5, 5, 4, 5]
}

df = pd.DataFrame(data)

# Line Chart for learning hours over days
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['Learning_Hours'], marker='o', linestyle='-', color='blue')
plt.title('Learning Hours over Days')
plt.xlabel('Date')
plt.ylabel('Learning hours')
plt.xticks(rotation=45)
plt.savefig('figures/learning_hours_over_days.png', bbox_inches='tight')
plt.show()

# Bar chart for Namaz offered per day
plt.figure(figsize=(12, 6))
plt.bar(df['Date'], df['Namaz_Offered'], color='green')
plt.title('Namaz offered per day')
plt.xlabel('Date')
plt.ylabel('Number of Namaz offered')
plt.xticks(rotation=45)
plt.savefig('figures/namaz_offered.png', bbox_inches='tight')
plt.show()

# Pie chart for proportion of different activities
plt.figure(figsize=(8, 8))
activity_counts = {
    'Sleep': df['Sleep_Hours'].sum(),
    'Quran': df['Quran_Minutes'].sum(),
    'Learning': df['Learning_Hours'].sum(),
    'English': df['English_Minutes'].sum(),
    'Namaz': df['Namaz_Offered'].sum()
}
plt.pie(activity_counts.values(), labels=activity_counts.keys(), startangle=140, colors=['red', 'blue', 'green', 'orange', 'purple'])
plt.title('Proportion of Different Activities')
plt.axis('equal') # Equal aspect ratio ensures that pie chart is circular.
plt.savefig('figures/activity_proportions.png', bbox_inches='tight')
plt.show()

# Scatter plot for sleep hours and mood rating
plt.figure(figsize=(10, 6))
plt.scatter(df['Sleep_Hours'], df['Mood_Rating'], color='purple', s=100)
plt.title('Sleep Hours vs Mood Rating')
plt.xlabel('Sleep Hours')
plt.ylabel('Mood Rating')
plt.savefig('figures/sleep_vs_mood.png', bbox_inches='tight')
plt.show()
