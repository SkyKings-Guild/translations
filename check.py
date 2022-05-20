import json

with open('encodings.json', 'r') as f:
    encodings = json.load(f)
    

for lang, encoding in encodings.items():
    with open(f'translations/{lang}.json', 'r', encoding=encoding) as f:
        json.load(f)
        print(f'translations/{lang}.json OK')
