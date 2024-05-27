import os
import sys
# os.sys.path.insert(0, os.getcwd().split('/dags')[0])
os.sys.path.append("/home/sunnytan/project/dw_etl_airflow")

from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
from airflow.decorators import dag
from airflow import DAG
import extract_test
import transform 
import load
import cleanup 
import pendulum

@dag(
    default_args={
        'depends_on_past': False,
        'retries': 0,
        'retry_delay': timedelta(minutes=5),
    },
    dag_id='twitter_wh_dag',
    tags=["twitter"],
    description='DAG to extract, transform and load data to Twitter Data Warehouse',
    schedule=timedelta(days=7),
    start_date=pendulum.datetime(pendulum.today().year, pendulum.today().month, pendulum.today().day ,tz="UTC")
)
def TwitterWHDAG():
    extract_task = extract_test.LoadToStaging()
    transform_task =transform.TransformData()
    load_task = load.LoadToDW()
    cleanup_task = cleanup.CleanUP()

    extract_task >> transform_task >> load_task >> cleanup_task

d = TwitterWHDAG()