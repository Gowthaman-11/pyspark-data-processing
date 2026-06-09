from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("PySparkETL").getOrCreate()

df = spark.read.csv("input.csv", header=True)

df.show()

spark.stop()
