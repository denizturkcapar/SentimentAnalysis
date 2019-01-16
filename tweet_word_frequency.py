'''
In this program, I created a word cloud from sample tweet data
provided by the Girls Who Code organization with my students at Girls Who Code.
This program first prints words with their frequency counts and then generates a wordcloud from the words in the tweets.
The frequency counts do not include unnecessary words -such as https- so that
we get a better idea of which meaningful words are used the most in tweets. Such words are filtered out using the variable wordsToFilter.

The second part of this project uses the wordcloud library to practice data visualization.
The wordcloud does not include the filtered words by design so that it is more reflective of how data is stored for my students

For this program, you will need JSON, TextBlob, matplotlib, and WordCloud.
You need to run python3 -m textblob.download_corpora to download the Textblob library
You also need the tweets_small JSON file in the same folder to run this program.
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud



#Reads and loads the JSON data
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
# closes the JSON file
tweetFile.close()

#Combines All the Tweet Texts
combinedTweets = ""
for tweet in tweetData:
	combinedTweets += tweet['text']

#Creates a Combined Tweet Blob
tweetblob = TextBlob(combinedTweets)


#Filter Words to see the frequencies of meaningful words. The words to be filtered are decided based on students' responses.
# The wordcloud is designed to include all the words without the word filter.
filtered_words = ["and", "thus", "hence", "while", "then", "about", "https", "the", "thing", "will", "could", "are", "automation", "is", "in"]
words_with_frequencies = {}

for word in tweetblob.words:
	#skips words in our filter
	if word.lower() in filtered_words:
		continue
	#skips words with numbers or random characters
	if not word.isalpha():
		continue

	#Make the words uniformly lowercase and add the frequency count
	words_with_frequencies[word.lower()] = tweetblob.word_counts[word.lower()]

# prints the words and their frequencies
print(words_with_frequencies)


#Creates the wordcloud
wc = WordCloud().generate(combinedTweets)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
