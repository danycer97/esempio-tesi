import pyspark
import pandas as pd
from pyspark.sql import SparkSession

pd.read_csv('test_dataset.csv')

spark = SparkSession.builder.appName('test').getOrCreate()
