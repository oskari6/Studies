# ETL extract, transform, load

"""
setup
airflow db init
airflow users create --username admin --password admin --firstname admin --lastname admin --role Admin --email admin@example.com
airflow webserver --port 8080
airflow scheduler

place the DAG in the /dags folder
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract_data():
    print("extracting")

def transform():
    pass
def load_data():
    pass

default_args = {"start_date", datetime(2023, 1, 1)}
dag = DAG("etl_pipeline", default_args=default_args, schedule_intercal="@daily")

extract_task = PythonOperator(task_id="extract", python_callable=extract_data, dag=dag)
transform_task = PythonOperator(task_id="transform", python_callable=transform, dag=dag)
load_task = PythonOperator(task_id="load", python_callable=load_data, dag=dag)

extract_task >> transform_task >> load_task

# luigi
import luigi

class ExtractData(luigi.Task):
    def output(self):
        return luigi.LocalTarget("data.csv")
    
    def run(self):
        with self.output().open("w") as f:
            f.write("id,name,price\n1,Apple,100\n2,Banana,50")

class TransformData(luigi.Task):
    def requires(self):
        return ExtractData()
    def output(self):
        return luigi.LocalTarget("transformed_data.csv")
    
    def run(self):
        with self.input().open("r") as infile, self.output().open("w") as outfile:
            for line in infile:
                if "price" not in line:
                    id, name ,price = line.strip().split(",")
                    outfile.write(f"{id},{name},{float(price)*1.2}\n")

class LoadData(luigi.Task):
    def requires(self):
        return TransformData()
    
    def output(self):
        return luigi.LocalTarget("databaes.txt")
    
    def run(self):
        with self.input().open("r") as infile, self.output().open("w") as outfile:
            outfile.write("loaded data:\n")
            for line in infile:
                outfile.write(line)

if __name__ == "__main__":
    luigi.run(["LoadData"])