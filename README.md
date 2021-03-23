# Twitter
Team 2 Project

Twitter Content Analysis – Pizza Motivation
Use Case Description
	Our pizza shoppe would like to find some new marketing opportunities to target potential customers. We would like to better understand our potential customer bases and how we can target to them. More specifically, we would like to explore sentiment related to purchasing pizza so that we can target specific motivations with targeted marketing campaigns. For example, if it is common for someone to tweet about watching a game and eating pizza with beer, we may want to create a marketing campaign with visuals of pizza, beer, and game watching, or market our pizza in the same timeframe as commercials showing the upcoming games. 
Project Description
	Based on our use case, we will use Tweet content analysis to analyze motivations and associations with pizza consumption. The steps for our project are as follows:
1.	Collect Data [Twitter API]
2.	Create data visualizations [matplotlib]
3.	Tokenize Data [Textblob]
4.	Clean the data – remove non-english tweets, remove stop words, stem the words, remove @mentions, URLs, and RT/Retweet, unnecessary characters, etc. [pandas and Textblob]
5.	Add n-grams which will be used as features, then apply Tf-Idf which converts the n-grams into numbers that reflect their frequency within the tweet and inverse of frequency within the set. This is mapped as a matrix. 
6.	Map the coordinates with MDS (multidimensional scaling) [sklearn]
7.	Cluster the map with K-means to identify clusters – with this, we can find the words most commonly associated with the top clusters. [sklearn]
8.	Visulize the results and optimize[matplotlib, sklearn]
9.	Interpret the Results
Initial Data Visualizations from Data Exploration
 
 ![image](https://user-images.githubusercontent.com/80725922/112228986-285cef80-8c00-11eb-970e-e4f0b3fff3c5.png)
 ![image](https://user-images.githubusercontent.com/80725922/112229047-41fe3700-8c00-11eb-9582-d58e917aac4e.png)
![image](https://user-images.githubusercontent.com/80725922/112229064-46c2eb00-8c00-11eb-8d1e-4f10d0355969.png)


 
Useful Data Features
	The data selected includes datetime and tweet content. Additionally, we were able to apply textblob sentiment which provides subjectivity and polarity for each tweet. Subjectivity assigns a score between 0 and 1 that scores how subjective vs. objective a tweet is. Polarity assigns a score between -1 and 1 that score how negative, neutral, or positive a tweet is. Once we add the n-grams, an additional feature will be common word sequences. 

Data Sources
	The data comes directly from Twitter, using a developers code and log in keys we were able to download tweets that included the hashtag “pizza” and was the most recent up to 10,000 tweets.


[Twitter Content Analysis.docx](https://github.com/Machine-Learning-Final/Twitter/files/6193175/Twitter.Content.Analysis.docx)
