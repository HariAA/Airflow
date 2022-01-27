# Airflow Set up Azure Kubernetes
# Introduction
  This set up covers set up instruction to install and configure airflow on Azure Kubernetes Services. I have installed airflow version 2.0 version on AKS.
  The below section covers the following areas:
  1. Infra Requirement
  2. Prepare Airflow image
  3. Azure Enterprise Applicatio Changes
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
