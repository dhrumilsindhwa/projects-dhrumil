# Trivia ETL Pipeline

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using the Open Trivia API, Python, and Plotly for data visualization. The pipeline extracts trivia questions, transforms the data into a structured format, and visualizes the data using interactive charts.

## Overview

1. **Extract**: Data is extracted from the Open Trivia API.
2. **Transform**: The extracted data is transformed into a structured format using Python and pandas.
3. **Visualize**: The transformed data is visualized using Plotly, generating interactive charts to analyze question categories and difficulty distribution.

## Dependencies

- Python 3.x
- pandas
- requests
- plotly

To install the required libraries, run the following command:

```bash
pip install pandas requests plotly


Steps
Extract data from the Open Trivia API: 
The pipeline sends a request to the Open Trivia API, fetching 50 multiple-choice trivia questions. 
The received data is in JSON format.

Transform the data: The JSON data is parsed and transformed into a pandas DataFrame, which simplifies data manipulation. 
The questions and answers are cleaned of any HTML entities. 
The final DataFrame contains the following columns: 'category', 'difficulty', 'question', 'correct_answer', and 'incorrect_answers'.

Visualize the data using Plotly: 
The transformed data is used to create a bar chart displaying the count of questions per category, and a pie chart showing the distribution of question difficulty. 
The visualizations are combined in a subplot and saved as an interactive HTML file.
