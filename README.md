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
	

Machine Learning Algorithms

NGrams
We applied Ngrams to our dataset. Ngrams are just word combinations, meaning words that appear together sequentially, so you can have a bigram which is two words, or trigram which is 3 words and so on. This step just added some additional diversity into our corpus and also helps us to identify sets of words in our topic that appear together. We used bigrams and trigrams.

 <img width="393" alt="Screen Shot 2021-04-30 at 2 49 00 PM" src="https://user-images.githubusercontent.com/80725922/116747244-394d0d80-a9c3-11eb-8584-ffb4d317f3cc.png">


Count Vectorizer
We then applied the spark count vectorizer model to our dataframe which converts the collection of documents (tweets) to vectors of token counts. During the fitting process, CountVectorizer selects to the top vocabsize words ordered by term frequency across the corpus and the result is a sparse vector. In order to make the machine learning model work, we needed to convert the sparse vector to a dense vector as that is the format that our model takes.


LDA (Latent Dirichlet Allocation)
We had originally planned to use K-means to find clusters of words that we would make recommendations on for our use case, but we ran into an issue because Spark does not have multidimensional scaling which we needed in order to effectively apply K-means to our dataset. So we researched alternatives and chose latent dirichlet allocation. LDA is also an unspervised clustering algorithm that models documents and topics based on Dirichlet distribution. It iteratively searches a set of documents, in our case tweets, to identify topics that best describe the set of documents. So with that, we are able to identify topics we can use to make marketing campaigns around based on tweets.
When we apply the LDA model, we get a set of topics and associated words with a number that indicates the weight of that word or ngram for that topic. 
Within this model, we can set k as however many topics we would like the LDA model to describe and as many words as we would like to include. After exploring multiple combinations of k topics and n number of words, we finally set k topics to 3 and chose to show the top 10 words or ngrams associated with that topic.

<img width="207" alt="Screen Shot 2021-04-30 at 2 55 06 PM" src="https://user-images.githubusercontent.com/80725922/116747788-10794800-a9c4-11eb-9426-655494233ef4.png">



Recommendations

From the 3 topics that we chose, we identified the key words that would help us make business recommendations. The themes were:
1. Pineapple pizza
2. Make pizza
3. Food with friends
And a common theme between all of these was order/time/call

Therefore, we made the following business recommendations:

PRODUCT DEVELOPMENT
Perform cross selling with pineapple pizza as the base
Include a DIY pizza kit as part of the new product offerings

MARKETING
Campaign featuring a pineapple pizza combo
Campaign with friends or couples making pizza from the kit

CUSTOMER EXPERIENCE
Improve delivery experience by making it faster and seamless


Shortcomings & Improvements

SHORTCOMINGS
Non-English words and non-words
Similarities between words in topics
No events found
Pivoted due to lack of native multidimensional scaling in Spark\

IMPROVEMENTS
Use another Tweet extraction method
Filter only English language
Add hashtags that would include events
Sample a more comprehensive time frame
Include location information
Remove "pizza" as a stop-word

 
 


[Twitter Content Analysis.docx](https://github.com/Machine-Learning-Final/Twitter/files/6193175/Twitter.Content.Analysis.docx)
