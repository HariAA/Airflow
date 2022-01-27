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
  
 # Azure Enterprise Application Changes
 The Airflow webserver comes with basic authentication. I wanted to integrate airflow webserver with Azure AD authentication. In addition to that we can also set up users and roles in Azure AD which can be sycned to airflow webserver when starting up. This way you can manage users and roles to airflow centrally in Azure AD. In order to do this you have to do the following:
  1. Go to Azure Directory and create new App registration
  2. Under the redirect url, give the path to the airflow webserver (to be configured after webserver is up running)
  3. Go to API permission and give permission and give permission on Microsoft Graph - OpenID, Profile and User.read. This helps in reading the user details when you sign in to webserver
  4. Go to App Roles and create appropriate roles as per your need. I have created Admin and Viewer
  5. Go to Enterprise Application and under Users and Groups add the users and select the Role defined in the above step.
  6. Note down the ServicePrinciple, object id, secret
    
 # Changes to Values.yaml
  For installing airflow and its services, values.yaml file is the only place where you configure everything that you need. It comes pre-loaded with many parameters which you can change or add on top according to your need. I will explain below the key changes i have done 
  ### Executor: 
   Since airflow is running on AKS i have set this value to KubernetesExecutor
  ### Images-->Airflow-->Repository:
   I have given path to my custom image hosted in my azure container registry
  ### Data-->metadataSecretName:
   This is used to store the connection details to the postgres sql for airflow backend. I have created a secret in AKS to store the connection details. And referred the secret name here in this place
  ### webserverConfig:
   Majority of the code related to authentication and authorization happens here. I have written a Custom Airflow Security Manager class which uses flask app builder api to override the key function to handle azure integration
   1. get_oauth_user_info: returns a dictionary of logged in user details along with his role
   2. AUTH_ROLES_MAPPING: This maps the Azure Roles to airflow roles
   3. OAUTH_PROVIDERS: A Dictionary which contains connection details to the Azure AD Tenant and Service principal id and secret
  ### Registry-->secretName:
   This contains the connection details to the Azure Container Registry. I have created a AKS secret to store the connection details and shared the secret name in this place
  ### Config--> Logging:
   Use this section to set remote loggin info. Set remote logging to True, remote base log folder to the container name in the storage account, remote log conn id to the airflow connection id
  ### Dags-->gitSync:
   Use this section to set up connection to the git repository where the dags are stored. Airflow syncs the dag every fixed interval. Update repo to your git repo, branch name, credentialsecret to aks secret which contains the git connection details.
 
 ## Set up Instructions:
 
 The
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
