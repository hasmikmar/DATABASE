from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.models import Variable
from datetime import datetime, timedelta


default_args = {
    'owner': 'Hasmik',
    'depends_on_past': False,
    'email': ['hasmik_margaryan@de.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
with DAG(
    dag_id='pyspark_etl_daily',
    default_args=default_args,
    description='Daily ETL job for ad impressions and events',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=True,
    tags=['pyspark', 'etl', 'ads']
) as dag:

    run_pyspark_etl = BashOperator(
        task_id='run_pyspark_etl',
        bash_command='python3 /Users/hasmikmargaryan/Desktop/DE_TASK/spark_jobs/process_impressions.py'
    )

    run_pyspark_etl
