import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('trivia_questions.csv')

# Count the number of questions in each category
category_counts = df['category'].value_counts()

# Create a bar chart
plt.bar(category_counts.index, category_counts.values)

# Add labels and title
plt.xlabel('Category')
plt.ylabel('Number of Questions')
plt.title('Distribution of Categories')

# Rotate x-axis labels for better readability
plt.xticks(rotation=90)

# Show the plot
plt.show()
