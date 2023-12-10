import json

with open('Grove.json', 'r', encoding='utf-8') as f1, open('personNew.json', 'r', encoding='utf-8') as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)

name_to_gang = {item['connectedNode']['properties']['name']: 'Гроув стрит' for item in data1}

for item in data2:
    name = item['Name']
    if name in name_to_gang:
        item['Gang'] = name_to_gang[name]

with open('personNew.json', 'w', encoding='utf-8') as output_file:
    json.dump(data2, output_file, indent=2, ensure_ascii=False)