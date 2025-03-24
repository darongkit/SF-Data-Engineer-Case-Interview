# Scheduler Libraries
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Data Processing Libraries
import csv
import pandas as pd
import numpy as np

# Define the default arguments dictionary
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2025, 3, 24),  # Set your start date here
}

# Define the DAG
dag = DAG(
    'Section1',  # DAG name
    default_args=default_args,
    description='process and output data files on daily interval',
    schedule_interval='0 1 * * *',  # Run every day at 1 AM
    catchup=False,  # Don't backfill past DAG runs
)

# Define your tasks
start_task = DummyOperator(
    task_id='start',
    dag=dag,
)

def process_datasets():
    # Read Datasets--------------------------------------------
    df1 = pd.read_csv('/opt/airflow/csv_files/dataset1.csv')
    df2 = pd.read_csv('/opt/airflow/csv_files/dataset2.csv')

    print(df1.head())
    print(df2.head())

    # Process dataset1.csv--------------------------------------------
    # Clean NaN or empty names and price = 0
    df1_cleaned = df1[(df1['name'].notna()) & (df1['name'] != '') & (df1['price'] != 0)]

    # Split name into first_name and last_name
    df1_cleaned[['first_name', 'last_name']] = df1_cleaned['name'].str.split(' ', expand=True)

    # Remove name column
    df1_cleaned = df1_cleaned.drop(columns=['name']) 

    # Reorder columns
    df1_cleaned = df1_cleaned[['first_name', 'last_name', 'price']]
    df1_cleaned['above_100'] = df1_cleaned['price'] > 100

    print(df1_cleaned.head(10))

    # Process dataset2.csv--------------------------------------------
    # Clean NaN or empty names and price = 0
    df2_cleaned = df2[(df2['name'].notna()) & (df2['name'] != '') & (df2['price'] != 0)]

    # Split name into first_name and last_name
    df2_cleaned[['first_name', 'last_name']] = df2_cleaned['name'].str.split(' ', expand=True)

    # Remove name column
    df2_cleaned = df2_cleaned.drop(columns=['name']) 

    # Reorder columns
    df2_cleaned = df2_cleaned[['first_name', 'last_name', 'price']]
    df2_cleaned['above_100'] = df2_cleaned['price'] > 100

    print(df2_cleaned)

    # Output processed dataframe--------------------------------------------
    df1_cleaned.to_csv('/opt/airflow/csv_files/processed_dataset1.csv', index=False)
    df2_cleaned.to_csv('/opt/airflow/csv_files/processed_dataset2.csv', index=False)

    # End--------------------------------------------

python_task = PythonOperator(
    task_id='Section1',
    python_callable=process_datasets,
    dag=dag,
)

# Set task dependencies
start_task >> python_task
