import re
import time
from pyspark import SparkConf, SparkContext, SQLContext
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

conf = SparkConf().setMaster("local").setAppName("DataCorrectness")
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

start_time = time.time()

file_path = "../../../../../../Downloads/edi-contacts.csv"

schema = StructType([
    StructField("id", IntegerType(), True),
    StructField("firstname", StringType(), True),
    StructField("lastname", StringType(), True)])

contacts_df = sqlContext.read.csv(file_path, header=False, schema=schema)

pattern = "^[A-Za-z0-9 ;&'-]+$"
contacts_df = contacts_df.withColumn("Flag", contacts_df.firstname.rlike(pattern) & contacts_df.lastname.rlike(pattern)).filter("Flag == 'False'")

ouput_file_path = "../../../../../../Downloads/spark-flagged-edi-contacts-dir"
contacts_df.coalesce(1).write.csv(ouput_file_path, header=True)

# contacts_df.toPandas().to_csv(ouput_file_path)

print("--- %s seconds ---" % (time.time() - start_time))