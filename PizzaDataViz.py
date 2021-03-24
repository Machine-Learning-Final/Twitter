import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import datetime as dt
from textblob import TextBlob

colnames = ['datetime','tweet_content']

df = pd.read_csv("~/pizza.csv", names=colnames, header=None)
df['sentiment'] = df['tweet_content'].apply(lambda tweet: TextBlob(tweet).sentiment)

df['counts'] = df.groupby('datetime', as_index=False)['datetime'].transform(lambda s: s.count())

x = []; y=[]
for point in df['sentiment']:
   x.append(point[0])
   y.append(point[1])
    

plt.figure(figsize=(10, 10))
plt.scatter(x, y, alpha=0.5)
plt.title("Sentiment:Polarity vs. Subjectivity")
plt.xlabel("Polarity")
plt.ylabel("Subjectivity")
plt.show()

plt.figure(figsize=(10, 10))
sns.lineplot(x="datetime", y="counts", data=df)
plt.xticks(rotation=15)
plt.title('Count of Tweet Times By Minute')
plt.xlabel('Time(Minutes)')
plt.ylabel('Count')
plt.show()

df['datetime'] = pd.to_datetime(df['datetime'], format='%m/%d/%y %H:%M').dt.hour
plt.figure(figsize=(10, 10))
sns.lineplot(x="datetime", y="counts", data=df)
plt.xticks(rotation=15)
plt.title('Count of Tweet Times By Hour')
plt.xlabel('Time(Hours)')
plt.ylabel('Count')
plt.show()