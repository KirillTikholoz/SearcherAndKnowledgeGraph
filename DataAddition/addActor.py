import json

with open('Actors.json', 'r', encoding='utf-8') as f1, open('testPersonForActors.json', 'r', encoding='utf-8') as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)

name_to_business = {item['n']['properties']['name']: item['n']['properties'].get('Business', None) for item in data1}

for item in data2:
    name = item['Name']
    business_value = name_to_business.get(name)

    if business_value is not None:
        if "Актер" not in item['Business']:
            item['Business'].append("Актер")

with open('updated_file2_business.json', 'w') as output_file:
    json.dump(data2, output_file, indent=2, ensure_ascii=False)