# Airflow Set up Azure Kubernetes
# Introduction
  This set up covers set up instruction to install and configure airflow on Azure Kubernetes Services. I have installed airflow version 2.0 version on AKS.
  The below section covers the following areas:
  1. Infra Requirement
  2. Prepare Airflow image
  3. Azure Enterprise Application Changes
  4. Changes to Values.yaml
  5. Set up Instruction

# Infra Requirement
  In order to set up airflow on AKS, i have used the following azure services
   - AKS - Azure Kubernetes Service with a single basic VM. This would host the airflow webserver and scheduler pods and the ingress controller pods
   - Postgres - Azure Database for Postgres to set up the backend database for airflow server. This will store the airflow dag and execution details.
   - AzureContainerRegistry - Container Registry to store the airflow image. I have extended the base 2.0 image to add additional libraries
   - StorageAccount - Azure Storage account which will have container to capture the logs from airflow executios
   - GIT Repo: A git repo which will host all the airflow dags.
 
 # Prepare Airflow image
  The base image of airflow 2.0.0 didnt have databricks providers. So i created a custom image by extending the base image and adding databricks provider. The databricks provider is useful in submitting job on databricks compute. It uses the databricks jobs api to submit a job for execution on databricks cluster, monitors the run and reports the status back in the dag tree. There are other spark connectors which can be used to submit spark job on a open source implementation of spark using spark submit. I have build the image and deployed it on the Azure Container Registry
  
 # Azure Enterprice Application Changes
 
