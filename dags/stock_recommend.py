from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests

# Install requests if needed: pip install requests

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

def get_recommendations_stock(**kwargs):
    url = "https://api.example.com/first-endpoint"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for non-200 status codes
        
        print(f"First API response: {response.text}")
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error calling first API: {str(e)}")
        raise

def send_email(**kwargs):
    url = "https://api.example.com/second-endpoint"
    recommendation_data = kwargs['ti'].xcom_pull(task_ids='call_first_api')
    try:
        response = requests.get(url, json=recommendation_data)
        response.raise_for_status()
        
        print(f"Second API response: {response.text}")
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error calling second API: {str(e)}")
        raise

with DAG(
    'stock_recommendation_dag',
    default_args=default_args,
    description='DAG to call two different APIs',
    schedule_interval='0 0 * * 0',# Adjust as needed
    catchup=False
) as dag:
    
    call_api_1 = PythonOperator(
        task_id='call_first_api',
        python_callable=get_recommendations_stock
        provide_context=True 
    )
    
    call_api_2 = PythonOperator(
        task_id='call_second_api',
        python_callable=send_email
        provide_context=True 
    )

    # Set execution order (run sequentially)
    call_api_1 >> call_api_2
