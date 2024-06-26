import sys
sys.path.append('.')

import pandas as pd
import numpy as np
from src.module.data_processing import *

df = pd.read_csv('data/hackers_test/hackers_test_raw.csv', encoding='cp949')

df.drop(['Day', 'Unnamed: 4', 'Unnamed: 5', '외움'], axis=1, inplace=True)

df['뜻'] = df['뜻'].apply(remove_parentheses).apply(remove_whitespace).apply(remove_semicolon).apply(remove_comma)
df = df[~df['뜻'].str.contains('~')]
df.replace("", np.nan, inplace=True)
df.dropna(inplace=True)
dict = {row[0]: row[1] for row in df.itertuples(index=False)}


with open('data/hackers_test/hackers_test_processed.json', 'w', encoding='utf-8') as f:
    f.write(dict_to_json(dict))
