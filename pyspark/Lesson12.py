from pyspark.sql import SparkSession
import os
os.environ["PYSPARK_PYTHON"] = "D:\\python\\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = "D:\\python\\python.exe"

spark = ( SparkSession.builder
    .appName("LocalTest")
    .master("local[*]")
    .config("spark.driver.host", "127.0.0.1")
    .config("spark.driver.bindAddress", "127.0.0.1")
    .getOrCreate())

_options = {
    "header":"true",
    "inferSchema":"true",
    "mode":"PERMISSIVE"
}

df = spark.read.format("csv").options(**_options).load("D:/pycharm professional/workSpace/PythonMLProject/files/csv/user_data.csv")

df.createTempView("temp_table")

spark.sql("select age,count(1) as cnt from temp_table group by age").show(100)

spark.stop()