import os
from pyspark.sql import SparkSession

# 显式指定 Python 解释器路径
os.environ["PYSPARK_PYTHON"] = "D:\\python\\python.exe"
os.environ["PYSPARK_DRIVER_PYTHON"] = "D:\\python\\python.exe"

print(os.environ)