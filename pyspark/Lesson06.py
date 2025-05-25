from pyspark.sql.types import StructType,StructField,StringType,IntegerType

schema_spark = StructType([
    StructField("name", StringType(), True),
    StructField("age", IntegerType(), True)
])

from pyspark.sql.functions import col,expr