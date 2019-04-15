# -*- coding: utf-8 -*-
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
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.docker_operator import DockerOperator
from airflow.operators.dagrun_operator import TriggerDagRunOperator

default_args = {
	'owner': 'airflow',
	'depends_on_past': False,
	'start_date': datetime.utcnow(),
	'email': ['airflow@example.com'],
	'email_on_failure': False,
	'email_on_retry': False,
	'retries': 1,
	'retry_delay': timedelta(minutes=1)
	}

dag = DAG(
	'docker_sample', default_args=default_args, schedule_interval=timedelta(minutes=10))

t1 = BashOperator(
	task_id='print_date',
	bash_command='date',
	dag=dag)

t2 = BashOperator(
	task_id='sleep',
	bash_command='sleep 5',
	retries=3,
	dag=dag)

# docker run --rm -e SPARK_MASTER=spark://ajibd-spark-master:7077 --network ajibd_ajibd-spark-network -v $HOST_PREFIX/`pwd`/../docker-spark:/local -v $HOST_PREFIX/`pwd`/target/scala-2.11/:/project -e FILENAME="/local/UKSA_Oct_18_-_Transparency_Data.csv" ls12styler/myfirstscalaspark:latest

#t3 = DockerOperator(
#    api_version='1.39',
#    image='ls12styler/myfirstscalaspark:latest',
#    task_id='myfirstscalaspark',
#    environment={
#        "SPARK_MASTER": "spark://ajibd-spark-master:7077",
#        "FILENAME": "/local/UKSA_Oct_18_-_Transparency_Data.csv"
#    },
#    volumes=[
#        '/Users/broadlea/workspace/src/github.com/ls12styler/myfirstscalaspark/target/scala-2.11/:/project'
#    ],
#    dag=dag
#)
#t3 = DockerOperator(api_version='1.39',
#	command='/bin/sleep 30',
#	image='centos:latest',
#	network_mode='bridge',
#	task_id='docker_op_tester',
#	dag=dag)


#t4 = BashOperator(
#	task_id='print_hello',
#	bash_command='echo "hello world!!!"',
#	dag=dag)

def conditionally_trigger(context, dag_run_obj):
    """This function decides whether or not to Trigger the remote DAG"""
    return dag_run_obj

t5 = TriggerDagRunOperator(
        trigger_dag_id='second_dag',
        execution_date=datetime.utcnow(),
        dag=dag,
        python_callable=conditionally_trigger,
        params={'condition_param': True, 'message': 'Hello World'},
        task_id='run_second_dag')

t1 >> t2
t1 >> t5
#t1 >> t3 >> t4
