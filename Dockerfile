FROM apache/airflow:2.0.0
RUN pip install --no-cache-dir apache-airflow-providers-databricks
RUN pip install --no-cache-dir apache-airflow-providers-apache-spark
