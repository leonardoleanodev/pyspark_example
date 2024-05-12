from pyspark.sql import SparkSession

# Create SparkSession
spark : SparkSession =  SparkSession.builder \
                    .master("spark://172.18.0.2:7077") \
                    .appName("example") \
                    .getOrCreate()

# Parallelize data and collect
data = [0, 2, 3, 4, 6]
rdd_a = spark.sparkContext.parallelize(data, 2)
result = rdd_a.glom().collect() # glom ?


def mod(x):
    return (x,x*x)

rdd_b = spark.sparkContext.parallelize(range(2),2)
