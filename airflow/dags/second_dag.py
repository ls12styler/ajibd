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
	'second_dag', default_args=default_args, schedule_interval=timedelta(minutes=10))

t1s = BashOperator(
	task_id='print_date_second',
	bash_command='date',
	dag=dag)

t2s = BashOperator(
	task_id='sleep_second',
	bash_command='sleep 5',
	retries=3,
	dag=dag)

# docker run --rm -e SPARK_MASTER=spark://ajibd-spark-master:7077 --network ajibd_ajibd-spark-network -v $HOST_PREFIX/`pwd`/../docker-spark:/local -v $HOST_PREFIX/`pwd`/target/scala-2.11/:/project -e FILENAME="/local/UKSA_Oct_18_-_Transparency_Data.csv" ls12styler/myfirstscalaspark:latest

t1s >> t2s
