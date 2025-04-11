from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

def generate_data():
    from generate_data import generate_orders, generate_logs
    generate_orders()
    generate_logs()

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "ecomdata_pipeline",
    default_args=default_args,
    description="Pipeline ETL pour EcomData",
    schedule_interval=timedelta(hours=1),
    start_date=datetime(2025, 4, 7),
    catchup=False,
) as dag:
    generate_task = PythonOperator(
        task_id="generate_data",
        python_callable=generate_data,
    )

    nifi_task = BashOperator(
        task_id="trigger_nifi",
        bash_command="echo 'Déclencher NiFi ici (à configurer via API)'",
    )

    generate_task >> nifi_task