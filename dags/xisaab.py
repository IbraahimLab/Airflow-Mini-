from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def start(ti, **kwargs):
    print("TI type:", type(ti))
    ti.xcom_push(key="ibra", value=10)
    print("Starting number is 10 ...")

def add_five(ti, **kwargs):
    number = ti.xcom_pull(key="ibra", task_ids="start_task")
    new_number = number + 5
    ti.xcom_push(key="ibra", value=new_number)
    print("Added 5 to", number, "is", new_number)

def multiply_by_two(ti, **kwargs):
    number = ti.xcom_pull(key="ibra", task_ids="add_five_task")

    new_number = number * 2
    ti.xcom_push(key="ibra", value=new_number)
    print("Multiplied by 2 to", number, "is", new_number)

def subtract_four(ti, **kwargs):
    number = ti.xcom_pull(key="ibra", task_ids="multiply_by_two_task")
    new_number = number - 4
    ti.xcom_push(key="ibra", value=new_number)
    print("Subtracted 4 from", number, "is", new_number)

def square(ti, **kwargs):
    number = ti.xcom_pull(key="ibra", task_ids="subtract_four_task")
    new_number = number * number
    print("Squared", number, "is", new_number)


with DAG(
    "xisaab_dag",
    start_date=datetime(2025,5,5),
    schedule="@daily",

) as dag:
    
    t1=PythonOperator(task_id="start_task", python_callable=start , do_xcom_push=True)
    t2=PythonOperator(task_id="add_five_task", python_callable=add_five)
    t3=PythonOperator(task_id="multiply_by_two_task", python_callable=multiply_by_two)
    t4=PythonOperator(task_id="subtract_four_task", python_callable=subtract_four)
    t5=PythonOperator(task_id="square_task", python_callable=square)


  #the depedencies is looks like this 

    t1>> t2>> t3>> t4>> t5