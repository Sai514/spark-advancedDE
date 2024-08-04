from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("ReadCSV").getOrCreate()

# Read CSV file
df = spark.read.csv("path/to/your/file.csv", header=True, inferSchema=True)

# Show the data
df.show()