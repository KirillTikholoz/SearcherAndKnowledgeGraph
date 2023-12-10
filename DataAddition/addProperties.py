import json

with open('graphPerson.json', 'r', encoding='utf-8') as file1:
    data1 = json.load(file1)

with open('person.json', 'r', encoding='utf-8') as file2:
    data2 = json.load(file2)

name_to_data_mapping = {
    entity1['n']['properties']['name']: entity1['n']['properties']
    for entity1 in data1
    if 'n' in entity1 and 'properties' in entity1['n'] and 'name' in entity1['n']['properties']
}

for entity2 in data2:
    name = entity2.get('Name')
    if name in name_to_data_mapping:
        for key, value in name_to_data_mapping[name].items():
            if key not in ['name', 'id']:
                entity2[key] = value

try:
    with open('personNew.json', 'w', encoding='utf-8') as output_file:
        json.dump(data2, output_file, indent=2, ensure_ascii=False)

except UnicodeEncodeError as e:
    print(f"UnicodeEncodeError: {e}")