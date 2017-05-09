#from nltk.corpus import stopwords
import numpy as np
import pandas as pd

df=pd.read_csv('demonetization.csv', sep=',', usecols=["text", "id"])

rows=len(df)

for i in xrange(rows):
	text=str(df.loc[i]['text']).lower()
	df.replace(df.loc[i]['text'], text, inplace=True)

print df
