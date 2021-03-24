
"""
Created on Tue Mar 23 20:13:38 2021

@author: alexb
"""
from pyspark.sql.types import *
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, lower, regexp_replace
import matplotlib.pyplot as plt
from pyspark.sql import Row
import re

conf = SparkConf().setAppName("tweet Data App").setMaster("local")
sc = SparkContext(conf=conf)
spark = SparkSession(sc)

PATH = r"C:\Users\alexb\sPYDER\data"

def get_tweet_data():
    custom_schema = StructType([
        StructField("time", StringType(), True),
        StructField("tweet",  StringType(), True)
    ])
    from pyspark.sql import SQLContext

    sql_context = SQLContext(sc)

    tweet_df = sql_context.read \
        .format('com.databricks.spark.csv') \
        .options(header='false', delimiter=',') \
        .load("%s/pizza.csv" % PATH, schema = custom_schema)
    return tweet_df

tweets = get_tweet_data()
tweets.show()
tweets_clean= tweets.select('time', (lower(regexp_replace('tweet', "[^a-zA-Z\\s]", "")).alias('tweet')))
tweets_clean.show()
from pyspark.ml.feature import  Tokenizer, StopWordsRemover
tokenizer = Tokenizer(inputCol="tweet", outputCol="words")
wordsData = tokenizer.transform(tweets_clean)
wordsData.show()
remover = StopWordsRemover(inputCol='words', outputCol='words_clean')
df_words_no_stopw = remover.transform(wordsData).select('time', 'words_clean')
df_words_no_stopw.show()
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer(language='english')
stemmer_udf = udf(lambda tokens: [stemmer.stem(token) for token in tokens], ArrayType(StringType()))
df_stemmed = df_words_no_stopw.withColumn("words_stemmed", stemmer_udf("words_clean")).select('time', 'words_stemmed')
df_stemmed.show()
filter_length_udf = udf(lambda row: [x for x in row if len(x) >=4 ], ArrayType(StringType()))
df_final_words = df_stemmed.withColumn('words', filter_length_udf(col('words_stemmed')))
df_final_words.show()