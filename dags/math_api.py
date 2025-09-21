from airflow import DAG
from airflow.decorators import task
from datetime import datetime

with DAG(
    dag_id="math_api",
    start_date=datetime(2023, 1, 1),
    schedule="@daily",
    catchup=False,
) as dag:

    @task
    def start_number():
        midkaan=10
        print(f"Starting number: {midkaan}")
        return midkaan
    @task
    def add_five(number):
        natiijo=number + 5
        print(f"After adding 5 {number }: {natiijo} ")
        return natiijo
    @task
    def multiply_by_two(number):
        natiijo=number * 2
        print(f"After multiplying by 2 :{number} : {natiijo}")
        return natiijo
    @task
    def subtract_three(number):
        natiijo=number - 3
        print(f"After subtracting 3 {number} : {natiijo}")
        return natiijo
    @task
    def square(number):
        natiijo=number ** 2
        print(f"After squaring {number} : {natiijo}")
        return natiijo  
    
    # Define the task dependencies
    task1 = start_number()
    task2 = add_five(task1)
    task3 = multiply_by_two(task2)
    task4 = subtract_three(task3)
    task5 = square(task4)
