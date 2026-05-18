from airflow.sdk import dag
from airflow.providers.standard.operators.bash import BashOperator
from pendulum import datetime

default_args = {
    'owner': 'Arthur Andrade',
    'retries' : 2,
}

@dag(
    dag_id="nyc_taxi_dag",
    schedule="@daily",
    start_date=datetime(2024, 6, 1),
    catchup=False,
    tags=["nyc", "spark"],
    default_args=default_args
)
def nyc_taxi_dag():
    
    download_data = BashOperator(
        task_id="download_data",
        bash_command="""
            cd /usr/local/airflow/ingestion && \
            chmod +x ./download_files.sh && \
            bash ./download_files.sh
        """,
    )

    send_data_to_lake = BashOperator(
        task_id="send_data_to_lake",
        bash_command="""
            cd /usr/local/airflow/ingestion && \
            python send_remote.py
        """,
    )
    download_data >> send_data_to_lake

dag = nyc_taxi_dag()