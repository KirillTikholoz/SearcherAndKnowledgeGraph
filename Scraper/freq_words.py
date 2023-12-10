import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import json


# Чтение данных из JSON-файла
with open("person.json", encoding="utf-8") as file:
    all_person = json.load(file)

# Создаем список для хранения всех значений поля "Description"
# Создаем список для хранения всех значений поля "Description"
all_descriptions = []

# Проходим по каждой сущности в массиве
for entity in all_person:
    # Проверка наличия поля "Description" в каждой сущности
    if 'Name' in entity:
        # Извлечение значения поля "Description" из каждой сущности
        description_value = entity['Name']

        # Преобразование списка в строку, если это список
        if isinstance(description_value, list):
            description_value = ' '.join(map(str, description_value))

        all_descriptions.append(description_value)
    else:
        print('Поле "Description" отсутствует в одной из сущностей.')

# Объединяем все значения "Description" в одну строку
all_descriptions_text = ' '.join(all_descriptions)

# Удаление лишних пробелов и символов
cleaned_text = re.sub(r'\s+', ' ', all_descriptions_text).strip()

# Разделение текста на слова и подсчет частоты
words = re.findall(r'\b\w+\b', cleaned_text)
word_counts = Counter(words)

# Вывод 10 самых часто встречающихся слов
most_common_words = word_counts.most_common(6000)
print(f'[')
for word, count in most_common_words:
    print(f'"{word}",')
    #print(f'{word}: {count}')
print(f']')