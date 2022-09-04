import json

with open('encodings.json', 'r') as ef:
    encodings = json.load(ef)

# load in the base translation file (en-US)
with open(f'translations/en-US.json', 'r', encoding='utf-8') as file:
    en_us = json.load(file)


def match_keys(original: dict, data: dict, *, path: str):
    passed = True
    original_keys = set(original.keys())
    keys = set(data.keys())
    if original_keys != keys:
        missing = original_keys - keys
        extra = keys - original_keys
        if missing:
            print(f"Missing keys in {path}: " + ', '.join(missing))
        if extra:
            print(f"Extra keys in {path}: " + ', '.join(extra))
        passed = False
    for k, v in data.items():
        if k not in original:
            continue
        if not isinstance(v, type(original[k])):
            print(f"Incorrect object type at {path}/{k}")
            passed = False
            continue
        if isinstance(v, dict):
            r = match_keys(original[k], v, path=path + '/' + k)
            if passed:
                passed = r
        elif isinstance(v, list):
            if len(original[k]) != len(v):
                print(f"Incorrect list length at {path}/{k}")
                passed = False
    return passed


def check_file(locale, enc):
    with open(f'translations/{locale}.json', 'r', encoding=enc) as f:
        data = json.load(f)
    res = match_keys(en_us, data, path=locale)
    print(f'Completed check for {locale}')
    return res


failed = []

for lang, encoding in encodings.items():
    if not check_file(lang, encoding):
        failed.append(lang)

if failed:
    raise ValueError(f"Checks for {', '.join(failed)} failed")
