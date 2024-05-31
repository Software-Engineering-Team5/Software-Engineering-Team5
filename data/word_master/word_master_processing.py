import sys
sys.path.append('.')

import pandas as pd
import numpy as np
from src.module.data_processing import *

df = pd.read_csv('data/word_master/word_master_raw.csv', encoding='cp949')

df['의미'] = df['의미'].str.replace('^.{4}', '', regex=True)
df = df[~df['의미'].str.contains('~')]
df['의미'] = df['의미'].apply(remove_after_bracket).apply(remove_parentheses).apply(remove_semicolon).apply(remove_comma)
df = df[~df['의미'].str.contains(' ')]
df.replace("", np.nan, inplace=True)
df.dropna(inplace=True)
dict = {row[0]: row[1] for row in df.itertuples(index=False)}


with open('data/word_master/word_master_processed.json', 'w', encoding='utf-8') as f:
    f.write(dict_to_json(dict))
