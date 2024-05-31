import sys
sys.path.append('.')

import pandas as pd
import numpy as np
from src.module.data_processing import *

df = pd.read_csv('data/amazing_talker/amazing_talker_raw.csv', encoding='cp949')

df = df[~df['뜻'].str.contains('-')]
df['뜻'] = df['뜻'].apply(remove_parentheses).apply(remove_semicolon).apply(remove_comma)
df = df[~df['뜻'].str.contains(' ')]
df.replace("#NAME?", np.nan, inplace=True)
df.replace("n", np.nan, inplace=True)
df.replace("", np.nan, inplace=True)
df.dropna(inplace=True)

grouped_df = df.groupby("단계")

# Create three separate DataFrames for each level
level_1_df = grouped_df.get_group('초등')
level_2_df = grouped_df.get_group('중고')
level_3_df = grouped_df.get_group('전문')

dict = {row[0]: row[1] for row in df.itertuples(index=False)}
dict_1 = {row[0]: row[1] for row in level_1_df.itertuples(index=False)}
dict_2 = {row[0]: row[1] for row in level_2_df.itertuples(index=False)}
dict_3 = {row[0]: row[1] for row in level_3_df.itertuples(index=False)}

with open('data/amazing_talker/amazing_talker_processed.json', 'w', encoding='utf-8') as f:
    f.write(dict_to_json(dict))

with open('data/amazing_talker/amazing_talker_easy_processed.json', 'w', encoding='utf-8') as f:
    f.write(dict_to_json(dict_1))
    
with open('data/amazing_talker/amazing_talker_normal_processed.json', 'w', encoding='utf-8') as f:
    f.write(dict_to_json(dict_2))
    
with open('data/amazing_talker/amazing_talker_hard_processed.json', 'w', encoding='utf-8') as f:
    f.write(dict_to_json(dict_3))