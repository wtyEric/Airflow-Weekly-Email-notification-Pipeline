# Airflow Weekly Email Notification Pipeline

This project leverages Apache Airflow to build a pipeline that integrates a stock recommendations API, an LLM (Large Language Model) analysis API, and scheduling to deliver weekly email notifications. The notifications contain the results of the API analysis for stock recommendations.

## Features

- **Stock Recommendations API**: Fetches stock-related data and recommendations. (Source: [Weekly-Stock-Email-Recommendation-Pipeline](https://github.com/wtyEric/Weekly-Stock-Email-Recommendation-Pipeline))
- **LLM Analysis API**: Processes and analyzes stock data to generate insights. (Source: [LLM-Financial-AI-Agent](https://github.com/wtyEric/LLM-Financial-AI-agent))
- **Airflow Scheduling**: Automates the pipeline to run weekly and send email notifications with the analysis results.

## How It Works

1. **Data Collection**: The pipeline retrieves stock recommendations from the stock recommendations API.
2. **Data Analysis**: The retrieved data is analyzed using an LLM analysis API to generate meaningful insights.
3. **Email Notification**: The analyzed results are compiled into an email and sent to the designated recipients on a weekly schedule.


