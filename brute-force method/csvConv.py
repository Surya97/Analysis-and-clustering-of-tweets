from nltk.twitter.util import json2csv
input_file="tweets.20150430-223406.json"
with open(input_file) as fp:
	json2csv(fp,'tweets_text.csv',['text'])