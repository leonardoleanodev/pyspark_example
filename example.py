import findspark
findspark.find()
findspark.init()


from pyspark.sql import SparkSession

# Create SparkSession
spark = SparkSession.builder \
                    .master("spark://172.18.0.3:7077") \
                    .appName("example2") \
                    .getOrCreate()

# Parallelize data and collect
data = [0, 2, 3, 4, 6]
rdd_a = spark.sparkContext.parallelize(data, 2)
#result = rdd_a.glom().collect() # glom ?


def mod(x):
    return (x,x*x)

rdd_b = spark.sparkContext.parallelize(range(2),2)
#result_b = rdd_b.map(mod) # map  returning error?

# # rdd = spark.parallelize(range(2)).map(mod).take(10)

# print(rdd)
