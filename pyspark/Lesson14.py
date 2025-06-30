from pyspark.sql import SparkSession
import os

os.environ["PYSPARK_PYTHON"] = "D:\\python\\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = "D:\\python\\python.exe"
os.environ["JAVA_OPTS"] = "-XX:+UseG1GC -XX:MaxGCPauseMillis=200 -XX:G1HeapRegionSize=16M"
os.environ["PYSPARK_SUBMIT_ARGS"] = "--driver-java-options '-XX:+UseG1GC' pyspark-shell"

spark = (SparkSession.builder
         .appName("LocalTest")
         .master("local[*]")
         .config("spark.driver.host", "127.0.0.1")
         .config("spark.driver.bindAddress", "127.0.0.1")
         .getOrCreate())

df = spark.read.format("json").load("D:/pycharm professional/workSpace/PythonMLProject/files/json/Lesson14.json")
df.show()