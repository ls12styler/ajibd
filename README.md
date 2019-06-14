# A Jouney Into Big Data

A docker-compose and set of scripts to be used as part of my journey into Big Data. 

## With Apache Spark

This particular section takes a look at getting started with Apache Spark in Scala. You'll learn how to build a Spark application and run it on a Docker based Spark Cluster.

#### Parts

* [Part 1 - The first in a series of posts about getting know Apache Spark for Big Data Processing.](https://towardsdatascience.com/a-journey-into-big-data-with-apache-spark-part-1-5dfcc2bccdd2)
* [Part 2 - An introduction to building your first Apache Spark application with Scala to read from CSV files.](https://towardsdatascience.com/a-journey-into-big-data-with-apache-spark-part-2-4511aa19a900)

The compose file includes the setup of an Apache Spark cluster.
To bring up a cluster with 2 workers, run:
```
docker-compose up spark-master spark-worker --scale spark-worker=2
```
The Spark Master can be found at http://127.0.0.1:8080/.

## With Apache Superset

This section looks at using Superset as the presentation layer for our data.

Superset can be found at http://127.0.0.1:8088. The default user login is:
* Username: admin
* Password: admin

## With Apache Airflow

This section takes a look into the 'scheduling' & 'orchestration' of  ETL pipelines using Airflow.

Airflow can be found at http://127.0.0.1:8081.

# Gotchas

### Airflow Scheduler

Currently the scheduler needs to started manually by running the following:

```
docker exec -it ajibd_airflow_1 /bin/bash
airflow scheduler
```

### Airflow Docker Permissions

Airflow doesn't have permissions to use the Unix docker socket (at /var/run/docker.sock). The way around this is to create a new group called docker:
```
DOCKER_GROUP_ID=$(stat -c '%g' /var/run/docker.sock) &&  \
  groupadd -g $DOCKER_GROUP_ID docker && \
  usermod -a -G docker airflow
```

# TODO's

* Healthchecks on each service
* A default dashboard for Superset
* A default DAG for Airflow with the DockerOperator

### Bonus Points

* Get the Airflow scheduler running without having to execute manually
* A Second DAG to try the TriggerDagRunOperator
