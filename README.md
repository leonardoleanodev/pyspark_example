# Creating a bitnami/spark base jupyterlab with spark master and workers with docker-compose

## setting up

create the app directory where the jupyter.ipynb are going to be stored and data to be shared with the jupyterlab

```
mkdir app/
```

change the permission for the folder in order to jupyterlab can create files and administrate the content:

```
chmod -R 777 app/
```

build the images, running the command:

```
docker-compose build
```

## Run the environment

run everything for master, 1 worker and jupyterlab:

```
docker-compose up
```

it you wanto more workers, run:

```
docker-compose up --scale spark-worker=<Number of requested workers>
```

## hosts

spark-master UI: localhost:8080
jupyterlab: localhost:8888

## example of usage at the jupyterlab

```
from pyspark.sql import SparkSession

# Create SparkSession
spark : SparkSession =  SparkSession.builder \
                    .master("spark://spark-master:7077") \
                    .appName("example") \
                    .getOrCreate()

# Parallelize data and collect
data = [0, 2, 3, 4, 6]
rdd_a = spark.sparkContext.parallelize(data, 2)
result = rdd_a.glom().collect() # glom ?

print(result)
```

## references:

https://hub.docker.com/r/bitnami/spark

https://medium.com/@MarinAgli1/setting-up-a-spark-standalone-cluster-on-docker-in-layman-terms-8cbdc9fdd14b

https://medium.com/@SaphE/testing-apache-spark-locally-docker-compose-and-kubernetes-deployment-94d35a54f222

https://www.youtube.com/watch?v=mzQX2lg8FDs

https://www.youtube.com/watch?v=FteThJ-YvXk

https://hub.docker.com/r/bitnami/spark
