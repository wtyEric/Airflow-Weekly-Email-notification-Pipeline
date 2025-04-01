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


## Setup

1. **Create a `.env` file**  
   Create a new file named `.env` in the root directory and add the following lines:
   ```env
   AIRFLOW_IMAGE_NAME=apache/airflow:2.4.2
   AIRFLOW_UID=50000
   ```

  
2. **Start the Airflow services**  
    2.1 Run the following command to start the services using Docker Compose:
    ```bash 
    docker-compose up -d
    ```
  
    2.2 Create an Admin user:
    Use the following command to create an Admin user for Airflow:
    ```bash 
    docker-compose run airflow-worker airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin
    ```
  
    2.3 Access the Airflow Web UI:
    Once the services are running, you can access the Airflow web interface at http://localhost:8080. Log in using the credentials you created in the previous step.
     
