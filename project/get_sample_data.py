import json, codecs

with open('/Users\sawyer\Desktop/sample.json', 'r', encoding="utf-8") as load_f:
    line = load_f.read()
    print(line)
    load_f.close()