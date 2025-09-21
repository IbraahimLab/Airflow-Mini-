from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def preproccesing_model():
    print("Preprocessing model...")

def training_model():
    print("Training model...")


def evaluating_model():
    print("Evaluating model...")

with DAG(
    "myanimal_dag",
    start_date=datetime(2025,5,5),
    schedule="@daily",

) as dag:
    
    t1=PythonOperator(task_id="preprocessing_task", python_callable=preproccesing_model)
    t2=PythonOperator(task_id="training_task", python_callable=training_model)
    t3=PythonOperator(task_id="evaluating_task", python_callable=evaluating_model)


  #the depedencies is looks like this 

    t1>> t2>> t3
 
