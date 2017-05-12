from nltk.twitter import Twitter
tw=Twitter()
tw.tweets(to_screen=False, limit=20000, lang=['en'])