# Databricks notebook source
# MAGIC %run ./notebook.py

# COMMAND ----------

df = spark.read.csv('/mnt/crm_bronze/test_ppl/output_data/output.csv', header=True, inferSchema=True)

# COMMAND ----------

assert df.limit(1).collect().pop().asDict() == {
  'Name' : 'Guzman',
  'Age' : 26,
  'Birth_Year' : 1996
}
