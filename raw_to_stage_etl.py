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
    dag_id='Raw_To_Stage',
    default_args=default_args,
    description='DAG to run a script on a remote worker via Celery queue',
    schedule=None,  # manual trigger only
    start_date=datetime(2026, 1, 7),
    catchup=False,
    tags=['remote_worker'],
) as dag:

   run_remote_script = BashOperator(
    task_id='run_remote_script',
    bash_command='/opt/airflow/venv/py-env/bin/python "/opt/airflow/scripts/LEO%20AWS%20Migration/ETL/S3_Snowpipe_ETL/main_run.py"',
    queue='remote_queue',
   )

run_remote_script

