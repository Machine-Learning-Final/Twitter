#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 16:00:55 2021

@author: reginanavarro
"""


from pyspark.sql.types import *
from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, lower, regexp_replace, concat
import matplotlib.pyplot as plt
from pyspark.sql import Row
import re

conf = SparkConf().setAppName("tweet Data App").setMaster("local")
sc = SparkContext(conf=conf)
spark = SparkSession(sc)

PATH = r"/Users/reginanavarro/Desktop/"

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
tweets_clean= tweets.select('time', (lower(regexp_replace('tweet', "[^a-zA-Z\\s]", "")).alias('tweet')))

from pyspark.ml.feature import  Tokenizer, StopWordsRemover
tokenizer = Tokenizer(inputCol="tweet", outputCol="words")
wordsData = tokenizer.transform(tweets_clean)

remover = StopWordsRemover(inputCol='words', outputCol='words_clean')
df_words_no_stopw = remover.transform(wordsData).select('time', 'words_clean')

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer(language='english')
stemmer_udf = udf(lambda tokens: [stemmer.stem(token) for token in tokens], ArrayType(StringType()))
df_stemmed = df_words_no_stopw.withColumn("words_stemmed", stemmer_udf("words_clean")).select('time', 'words_stemmed')

filter_length_udf = udf(lambda row: [x for x in row if len(x) >=4 ], ArrayType(StringType()))
df_final_words = df_stemmed.withColumn('words2', filter_length_udf(col('words_stemmed')))
#--------------------------------------------------------------------------------------------------------

filter_length_udf = udf(lambda row: [x for x in row if len(x) <=10 ], ArrayType(StringType()))
df_final_words = df_final_words.withColumn('words', filter_length_udf(col('words2')))

df_final_words.show()
from pyspark.ml.feature import NGram
ngram = NGram(n=1, inputCol='words', outputCol='unigrams')
df_final_words = ngram.transform(df_final_words)
ngram = NGram(n=2, inputCol='words', outputCol='bigrams')
df_final_words = ngram.transform(df_final_words)
ngram = NGram(n=3, inputCol='words', outputCol='trigrams')
df_final_words = ngram.transform(df_final_words)

columns = ["time","words_stemmed","words","unigrams","bigrams","trigrams"]
df_final_words=df_final_words.select(concat(df_final_words.unigrams,df_final_words.bigrams,df_final_words.trigrams)
              .alias("ngrams"))

newdf = df_final_words.select("ngrams")
newdf.show()
#Drop unnecessary columns
df = newdf.drop("time", "words_stemmed", "words2", "words")
df = df.sample(.07)
print("sample")
df.show()
#Create Tweet ID
from pyspark.sql.functions import monotonically_increasing_id
df = df.withColumn("tweet_id", monotonically_increasing_id())
df.show()

#Count Vectorizer
from pyspark.ml.feature import CountVectorizer
cv = CountVectorizer(inputCol='ngrams', outputCol='features', vocabSize=100000, minDF=2)
cvmodel = cv.fit(df)
result = cvmodel.transform(df)
result.show()

from pyspark.mllib.linalg import Vectors as MLlibVectors
from pyspark.mllib.clustering import LDA as MLlibLDA

#Train the LDA model
model = MLlibLDA.train(
  result.select("tweet_id", "features").rdd.mapValues(MLlibVectors.fromML).map(list), k=3
)
#Show Topics and weights
topics = model.describeTopics(maxTermsPerTopic = 50)
for x, topic in enumerate(topics):
    print('topic number: ' + str(x))
    words = topic[0]
    weights = topic[1]
    for n in range(len(words)):
        print(cvmodel.vocabulary[words[n]] + ' ' + str(weights[n]))
