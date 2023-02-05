from pyspark.sql import SparkSession
spark = SparkSession\
        .builder\
        .appName("fantoir")\
        .getOrCreate()

spark.sparkContext.setLogLevel('WARN')

co = spark.read.parquet("/tmp/data/communes.parquet")
co.createOrReplaceTempView("commune")

res = spark.sql("SELECT ROW_NUMBER() OVER (ORDER BY code) as id, code, nom FROM commune LIMIT 10").collect()
		
for r in res:
	print(r)

spark.stop()
