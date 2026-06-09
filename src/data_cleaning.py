from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataCleaning").getOrCreate()

df = spark.read.csv("input.csv", header=True)

clean_df = df.dropDuplicates()

clean_df.show()

spark.stop()
