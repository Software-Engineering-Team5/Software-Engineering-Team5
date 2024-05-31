import sys
import json
sys.path.append('.')

# path = 'data/amazing_talker/amazing_talker_easy_processed.json'
# with open(path, 'r', encoding='utf-8') as f:
#     data = json.load(f)
    
# path = 'data/amazing_talker/amazing_talker_normal_processed.json'
# with open(path, 'r', encoding='utf-8') as f:
#     data = json.load(f)
    
# path = 'data/amazing_talker/amazing_talker_hard_processed.json'
# with open(path, 'r', encoding='utf-8') as f:
#     data = json.load(f)
    
path = 'data/amazing_talker/amazing_talker_processed.json'
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(data)
