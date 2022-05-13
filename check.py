import json

with open('encodings.json', 'r') as f:
    encodings = json.load(f)
    

for lang, encoding in encodings.items():
    with open(f'translations/{lang}.json', 'r') as f:
        json.load(f, encoding=encoding)
