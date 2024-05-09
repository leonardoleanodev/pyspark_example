from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf()
conf.setMaster("spark://spark-master:7077")
conf.setAppName("example")
sc = SparkContext(conf=conf)

def mod(x):
    return (x,x*x)

rdd = sc.parallelize(range(2)).map(mod).take(10)

print(rdd)
