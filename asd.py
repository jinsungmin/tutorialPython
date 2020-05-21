from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# data_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/housing/housing.data'
# df_data = pd.read_csv(data_url, sep='\s+', header = None)
#
# print(df_data)

from nltk.tokenize import WordPunctTokenizer
print(WordPunctTokenizer().tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))
