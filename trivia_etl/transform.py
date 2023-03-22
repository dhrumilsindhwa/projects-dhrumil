import requests
import pandas as pd

# Get trivia questions
api_url = "https://opentdb.com/api.php?amount=50&type=multiple"
response = requests.get(api_url)
data = response.json()

# Transform data
questions = []

for item in data['results']:
    question = {
        'category': item['category'],
        'difficulty': item['difficulty'],
        'question': item['question'],
        'correct_answer': item['correct_answer'],
        'incorrect_answers': ", ".join(item['incorrect_answers'])
    }
    questions.append(question)

# Create a DataFrame
df = pd.DataFrame(questions)

# Clean HTML entities in the questions and answers (e.g., '&quot;' to '"')
def clean_html(text):
    from html import unescape
    return unescape(text)

df['question'] = df['question'].apply(clean_html)
df['correct_answer'] = df['correct_answer'].apply(clean_html)
df['incorrect_answers'] = df['incorrect_answers'].apply(clean_html)

# Preview the transformed data
print(df.head())

# Save DataFrame to a CSV file
df.to_csv('trivia_questions.csv', index=False)


