# Databricks notebook source
from datetime import date
from pyspark.sql import functions as F
from pyspark.sql.types import IntegerType

# COMMAND ----------

df = spark.read.csv('/mnt/crm_bronze/test_ppl/input_data/sample.csv', header=True).withColumn('Age', F.col('Age').cast(IntegerType()))

# COMMAND ----------

def add_birth_year(age:int):
  c_year = date.today().year
  birth_year = c_year - age
  return birth_year

df = df.withColumn('Birth_Year', F.udf(add_birth_year)(F.col('Age')))

# COMMAND ----------

df.repartition(1).write.csv('/mnt/crm_bronze/test_ppl/output_data/output.csv', header=True, mode='overwrite')
