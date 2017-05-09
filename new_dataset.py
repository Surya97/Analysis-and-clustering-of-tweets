import numpy as np
import pandas as pd

df=pd.read_csv('demonetization.csv', sep=',', usecols=["text", "id"])

print df
