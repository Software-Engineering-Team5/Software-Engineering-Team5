import sys

sys.path.append('.')

from src.module.data_processing import *


def json_to_dict(file_name):
    path = 'data/' + file_name + '/' + file_name + '_easy_processed.json'
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

a = json_to_dict('amazing_talker')
print(a)