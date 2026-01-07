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
    start_date=datetime(2026, 01, 07),
    catchup=False,
    tags=['remote_worker'],
) as dag:

    run_remote_script = BashOperator(
        task_id='run_remote_script',
        bash_command='python /opt/airflow/scripts//LEO%20AWS%20Migration/prefect_flows/ETL/RAW_to_STAGE_ETL.py',
        queue='remote_queue',  # ensure this runs on the remote worker
    )

    run_remote_script

