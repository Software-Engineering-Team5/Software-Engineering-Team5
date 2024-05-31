import sys

sys.path.append('.')

from src.module.data_processing import *

a = json_to_dict('hackers_test')
print(a)