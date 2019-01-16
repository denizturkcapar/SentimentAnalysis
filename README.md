# SentimentAnalysis

In this project, I created a word cloud from sample tweet data
provided by the Girls Who Code organization with my students at Girls Who Code.
This program first prints words with their frequency counts and then generates a wordcloud from the words in the tweets.
The frequency counts do not include unnecessary words -such as https- so that
we get a better idea of which meaningful words are used the most in tweets. Such words are filtered out using the variable wordsToFilter.
The second part of this project uses the wordcloud library to practice data visualization.
The wordcloud does not include the filtered words by design so that it is more reflective of how data is stored for my students

# Requierements 
For this program, you will need 1) JSON, 2) TextBlob, 3) matplotlib, and 4) WordCloud.
You need to run python3 -m textblob.download_corpora to download the Textblob library
You also need the tweets_small JSON file in the same folder to run this program.
