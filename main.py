import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned dataset

df = pd.read_csv("cleaned_data.csv")

# Set chart style

sns.set_theme(style="whitegrid")

# Chart 1: Distribution of Workout Duration

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="Duration", bins=10, kde=True)
plt.title("Distribution of Workout Duration")
plt.xlabel("Duration (minutes)")
plt.ylabel("Number of Workouts")
plt.tight_layout()
plt.savefig("duration_distribution.png")
plt.show()
plt.close()

# Chart 2: Workout Duration vs Calories Burned

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x="Duration", y="Calories")
plt.title("Workout Duration vs Calories Burned")
plt.xlabel("Duration (minutes)")
plt.ylabel("Calories Burned")
plt.tight_layout()
plt.savefig("duration_vs_calories.png")
plt.show()
plt.close()

# Chart 3: Average Calories Burned by Duration

plt.figure(figsize=(8, 5))
sns.barplot(data=df, x="Duration", y="Calories", errorbar=None)
plt.title("Average Calories Burned by Workout Duration")
plt.xlabel("Duration (minutes)")
plt.ylabel("Average Calories Burned")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("average_calories.png")
plt.show()
plt.close()

print("\nAll 3 charts created successfully!")
