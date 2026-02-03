from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG
with DAG(
    dag_id='hello_demo',
    default_args=default_args,
    description='DAG to run a script on a remote worker via Celery queue',
    schedule=None,  # manual trigger only
    start_date=datetime(2026, 3, 2),
    catchup=False,
    tags=['remote_worker'],
) as dag:

   run_remote_script = BashOperator(
    task_id='hello_demo',
    bash_command='/opt/airflow/venv/py-env/bin/python "/opt/airflow/scripts/LEO%20AWS%20Migration/ETL/hello_demo.py"',
    queue='remote_queue',
   )

run_remote_script

