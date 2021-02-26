#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from datetime import datetime, timedelta
from airflow import dag
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator


dag = DAG(dag_id='test_bash', schedule_interval=None, start_date=datetime(2021,1,1),catchup=False)
dummy_task = DummyOperator(task_id='dummy_task',dag=dag)
bash_task = BashOperator(task_id='bash_task',bash_command="echo 'command executed from BashOperator'",dag=dag)
dummy_task >> bash_task