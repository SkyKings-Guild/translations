import json

with open('encodings.json', 'r') as ef:
    encodings = json.load(ef)

# load in the base translation file (en-US)
with open(f'translations/en-US.json', 'r', encoding='utf-8') as file:
    en_us = json.load(file)


def match_keys(original: dict, data: dict, *, path: str):
    original_keys = set(original.keys())
    keys = set(data.keys())
    if original_keys != keys:
        missing = original_keys - keys
        print(f"Missing keys in {path}: " + ', '.join(missing))
    for k, v in data.items():
        if not isinstance(v, type(original[k])):
            print(f"Incorrect object type at {path}/{k}")
            continue
        if isinstance(v, dict):
            match_keys(original[k], v, path=path + '/' + k)
        elif isinstance(v, list):
            if len(original[k]) != len(v):
                print(f"Incorrect list length at {path}/{k}")


def check_file(locale, enc):
    with open(f'translations/{locale}.json', 'r', encoding=enc) as f:
        data = json.load(f)
    match_keys(en_us, data, path=locale)
    print(f'Completed check for {locale}')


for lang, encoding in encodings.items():
    check_file(lang, encoding)
