import json
from elasticsearch import Elasticsearch

# Подключение к Elasticsearch
es = Elasticsearch("http://localhost:9200", timeout=120)

with open("names.json", encoding="utf-8") as fileNames:
    names = json.load(fileNames)

# Имя индекса
index_name = 'my_index'

def createIndex():
    mapping = {
        "mappings": {
            "properties": {
                "Name": {"type": "text", "analyzer": "my_custom_name_analyzer"},
                "Games": {"type": "text", "analyzer": "my_custom_game_analyzer"},
                "Business": {"type": "text", "analyzer": "my_custom_business_analyzer"},
                "Voiced": {"type": "text"},
                "Gender": {"type": "text", "analyzer": "my_custom_gender_analyzer"},
                "Nationality": {"type": "text"},
                "State": {"type": "text"},
                "Description": {"type": "text", "analyzer": "my_custom_analyzer"},

                "Gang": {"type": "text", "analyzer": "my_custom_analyzer"},
                "realname": {"type": "text", "analyzer": "my_custom_analyzer"},
                "alias": {"type": "text", "analyzer": "my_custom_analyzer"},
                "birthdate": {"type": "text", "analyzer": "my_custom_analyzer"},
                "language": {"type": "text", "analyzer": "my_custom_analyzer"},
                "englishname": {"type": "text", "analyzer": "my_custom_analyzer"},
                "musicpreferences": {"type": "text", "analyzer": "my_custom_analyzer"},
                "dislikes": {"type": "text", "analyzer": "my_custom_analyzer"},
                "role": {"type": "text", "analyzer": "my_custom_analyzer"},
                "occupation": {"type": "text", "analyzer": "my_custom_analyzer"},
                "такжеИзвестныйКак": {"type": "text", "analyzer": "my_custom_analyzer"},
                "residence": {"type": "text", "analyzer": "my_custom_analyzer"},
                "arabicname": {"type": "text", "analyzer": "my_custom_analyzer"},
                "wealth": {"type": "text", "analyzer": "my_custom_analyzer"},
                "birthplace": {"type": "text", "analyzer": "my_custom_analyzer"},
                "родился": {"type": "text", "analyzer": "my_custom_analyzer"},
                "birthyear": {"type": "text", "analyzer": "my_custom_analyzer"},
                "nickname": {"type": "text", "analyzer": "my_custom_analyzer"},
                "behavior": {"type": "text", "analyzer": "my_custom_analyzer"},
                "деньги": {"type": "text", "analyzer": "my_custom_analyzer"},
                "location": {"type": "text", "analyzer": "my_custom_analyzer"},
                "worksas": {"type": "text", "analyzer": "my_custom_analyzer"},
                "healthcondition": {"type": "text", "analyzer": "my_custom_analyzer"},
                "диджей": {"type": "text", "analyzer": "my_custom_analyzer"},
                "год": {"type": "text", "analyzer": "my_custom_analyzer"},
                "relationshipstatus": {"type": "text", "analyzer": "my_custom_analyzer"},
                "status": {"type": "text", "analyzer": "my_custom_analyzer"},
                "англ.имя": {"type": "text", "analyzer": "my_custom_analyzer"},
                "яп.имя": {"type": "text", "analyzer": "my_custom_analyzer"},
                "appearance": {"type": "text", "analyzer": "my_custom_analyzer"},
                "настоящееИмя": {"type": "text", "analyzer": "my_custom_analyzer"},
                "alsoknownas": {"type": "text", "analyzer": "my_custom_analyzer"},
                "currentgang": {"type": "text", "analyzer": "my_custom_analyzer"},
                "formergang": {"type": "text", "analyzer": "my_custom_analyzer"},
                "currentstatus": {"type": "text", "analyzer": "my_custom_analyzer"},
                "condition": {"type": "text", "analyzer": "my_custom_analyzer"},
                "age": {"type": "text", "analyzer": "my_custom_analyzer"},
                "полноеИмя": {"type": "text", "analyzer": "my_custom_analyzer"},
                "прозвище": {"type": "text", "analyzer": "my_custom_analyzer"},
                "criminalactivity": {"type": "text", "analyzer": "my_custom_analyzer"},
                "description": {"type": "text", "analyzer": "my_custom_analyzer"},
                "name(english)": {"type": "text", "analyzer": "my_custom_analyzer"},
                "biography": {"type": "text", "analyzer": "my_custom_analyzer"},
                "accent": {"type": "text", "analyzer": "my_custom_analyzer"},
                "mentalillness": {"type": "text", "analyzer": "my_custom_analyzer"},
            }
        },
        "settings": {
            "analysis": {
                "analyzer": {
                    "my_custom_analyzer": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": ["lowercase", "my_stemmer_filter", "my_synonym_filter"]
                    },
                    "my_custom_name_analyzer": {
                        "type": "custom",
                        "tokenizer": "keyword",
                        "filter": ["lowercase", "my_stemmer_filter", "my_synonym_name_filter", "russian_hunspell"]
                    },
                    "my_custom_game_analyzer": {
                        "type": "custom",
                        "tokenizer": "keyword",
                        "filter": ["lowercase", "my_stemmer_filter", "my_synonym_game_filter"]
                    },
                    "my_custom_gender_analyzer": {
                        "type": "custom",
                        "tokenizer": "keyword",
                        "filter": ["lowercase", "my_stemmer_filter", "my_synonym_gender_filter"]
                    },
                    "my_custom_business_analyzer": {
                        "type": "custom",
                        "tokenizer": "keyword",
                        "filter": ["lowercase", "my_stemmer_filter", "my_synonym_business_filter"]
                    }


                },
                "filter": {
                    "my_stemmer_filter": {"type": "stemmer", "name": "russian"},
                    "my_synonym_filter": {"type": "synonym", "synonyms": [
                        "персонаж, персона, личность, герой, индивид, фигура",
                        "время, период, длительность, хронометраж",
                        "является, представлен",
                        "миссии, задачи, цели, задания",
                        "игре, игровой процесс, геймплей, развлечение",
                        "семьи, родные, родственники",
                        "качестве, характеристика, свойство, атрибут, признак",
                        "игрок, участник",
                        "деньги, финансы, средства, капитал",
                        "года, годы, период, эпоха, век",
                        "смерти, конец, окончание",
                        "пытается, старается, усиливается, пытается достичь, стремится",
                        "момент, мгновение, период времени, момент времени, секунда",
                        "Online, сети, онлайн, подключенный к интернету",
                        "III, третий, третья, три, 3",
                        "IV, четвёртый, четвёртая, четыре, 4",
                        "V, пятый, пятая, пять, 5",
                        "Всего, сумме, всемирно",
                        "машину, автомобиль, транспортное средство, машина",
                        "жизни, существование, жизнедеятельность",
                        "клуба, общество, социальный клуб, группа",
                        "Которой, который, тот, который",
                        "конце, завершение, окончание, финал, конечный этап",
                        "звонит, звучит, звонок, вызов",
                        "игрок, геймер",
                        "событий, сценарий, происшествие, событие, случай",
                        "жизнь, существо, биение, бытие, существование",
                        "сайте, веб-сайт, онлайн-ресурс, интернет-ресурс, сайт",
                        "больше, более, дополнительно, ещё, превыше",
                        "встречает, встреча, встречаться, столкновение",
                        "денег, денежные средства, финансы, капитал, средства",
                        "клуб, общество, ассоциация, социальный клуб, группа",
                        "полиции, полицейские, силы безопасности",
                        "серии, последовательность, ряд, сериал, цикл",
                        "отношения, взаимоотношения, связь, отношение, соотношение",
                        "просто, легко, простота, простой, прямо",
                        "друг, товарищ, компаньон, приятель, союзник",
                        "Несмотря, вопреки, хотя"
                    ]},
                    "my_synonym_game_filter": {"type": "synonym", "synonyms": [
                        "GTA V, GTA 5, Grand Theft Auto V, Grand Theft Auto 5",
                        "GTA IV, GTA 4, Grand Theft Auto IV, Grand Theft Auto 4",
                        "GTA San Andreas, GTA SA, Grand Theft Auto: San Andreas, Grand Theft Auto SA, San Andreas",
                        "GTA Vice City, GTA VC, Grand Theft Auto: Vice City, Grand Theft Auto VC, Vice City",
                        "GTA Vice City Stories, GTA VCS, Grand Theft Auto: Vice City Stories, Grand Theft Auto VCS, Vice City Stories",
                        "GTA III, GTA 3, Grand Theft Auto III, Grand Theft Auto 3",
                        "GTA 2, Grand Theft Auto 2",
                        "GTA London, GTA London 1969, GTA London 1961, Grand Theft Auto: London, Grand Theft Auto: London 1969, Grand Theft Auto: London 1961",
                        "GTA Advance, Grand Theft Auto: Advance",
                        "GTA Liberty City Stories, GTA LCS, Grand Theft Auto: Liberty City Stories, Grand Theft Auto: LCS, Liberty City Stories",
                        "GTA Vice City Stories, GTA VCS, Grand Theft Auto Vice City Stories, Grand Theft Auto VCS, Vice City Stories",
                        "GTA Chinatown Wars, GTA CW, Grand Theft Auto Chinatown Wars, Grand Theft Auto CW, Chinatown Wars",
                        "GTA Online, Grand Theft Auto Online"
                    ]},
                    "my_synonym_gender_filter": {"type": "synonym", "synonyms": [
                        "муж, мужчина, м => мужчина",
                        "жен, женщина, ж => женщина",
                    ]},
                    "my_synonym_name_filter": {
                        "type": "synonym",
                        "synonyms": [
                            "Michael De Santa, Michael Townley, Michael, Mike => Майкл Де Санта",
                            "Trevor Philips, Trevor, T => Тревор Филипс",
                            "Franklin Clinton, Franklin, Frank => Франклин Клинтон",
                            "Niko Bellic, Niko => Нико Беллик",
                            "Tommy Vercetti, Tommy => Томми Версетти",
                            "CJ, Carl Johnson => Карл Джонсон",
                            "Big Smoke, Smoke => Мелвин Харрис",
                            "Carlito => Си Джей",
                            "Nikolai, Николай => Нико Беллик",
                            "Майкл Де Санта, Майкл Таунли, Майкл, Майк => Майкл Де Санта",
                            "Тревор Филипс, Тревор, Т => Тревор Филипс",
                            "Франклин Клинтон, Франклин, Фрэнк => Франклин Клинтон",
                            "Нико Беллик, Нико => Нико Беллик",
                            "Томми Верчетти, Томми => Томми Версетти",
                            "Си Джей, Карл Джонсон, Карлито => Карл Джонсон",
                            "Биг Смоук, Смоук => Мелвин Харрис"
                        ]
                    },
                    "my_synonym_business_filter": {
                        "type": "synonym",
                        "synonyms": [
                            "Торговля, коммерция, бизнес, обмен, продажа, сделка",
                            "Продажа, сбыт, сбыть, реализация, торговля",
                            "Оружие, вооружение, арсенал, боеприпасы, военные средства",
                            "Autos, автомобили, транспорт",
                            "Casino, казино, азартные игры, игорный дом",
                            "FM, радио, радиостанция, эфир",
                            "Казино, азарт",
                            "Ограбления, грабежи, ограбление, кража, набег",
                            "Ростовщичество, заемщик, кредитор, заимодавец, займ",
                            "Дон, главарь, босс, руководитель",
                            "Мафии, преступность, клан, группировка",
                            "Актёр, исполнитель, артист, киноактер",
                            "Угон, кража, автокража, похищение",
                            "мастерская, верфь, судостроение, судоремонт"
                        ]
                    },
                    "russian_hunspell": {
                        "type": "icu_folding",
                        "language": "ru_RU"
                    }

                }
            }
        }
    }


    es.indices.create(index=index_name, body=mapping)

    def index_data(document):
        try:
            es.index(index=index_name, body=document)
            print('Документ успешно проиндексирован:', document)
        except Exception as e:
            print('Ошибка при индексации документа:', e)

    file_path = 'C:\Programm2023\WebProg\DataAddition\personNew.json'

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for document in data:
            index_data(document)

    print('Чтение завершено.')

def deleteIndex():
    if es.indices.exists(index=index_name):
        # Удаляем индекс
        es.indices.delete(index=index_name)
        print(f"Индекс {index_name} успешно удален.")
    else:
        print(f"Индекс {index_name} не существует.")


def searchArticles(search_field, query):
    response = es.search(index=index_name, body={
        "query": {
            "bool": {
                "should": [
                    {
                        "multi_match": {
                            "query": query,
                            "fields": ["Games^2", "Description", "Business^2", "Voiced"
                                       "Gang^4", "realname", "alias", "birthdate", "language", "englishname",
                                       "musicpreferences", "dislikes", "role", "occupation", "такжеИзвестныйКак",
                                       "residence", "arabicname", "wealth", "birthplace", "родился", "birthyear",
                                       "nickname", "behavior", "деньги", "location", "worksas", "healthcondition",
                                       "диджей", "год", "relationshipstatus", "status", "англ.имя", "яп.имя",
                                       "appearance", "настоящееИмя", "alsoknownas", "currentgang", "formergang",
                                       "currentstatus", "condition", "age", "полноеИмя", "прозвище", "criminalactivity",
                                       "description", "name(english)",  "biography", "accent", "mentalillness"],
                            "fuzziness": "AUTO"
                        }
                    },
                    {
                        "match": {
                            "Name": {
                                "query": query,
                                "boost": 3.0
                                }
                        }
                    }
                ],
                "must_not": {
                    "terms": {
                        "Description": ["Юджин Рипер"]
                    }
                }
            }
        },
        "highlight": {
            "fields": {
                "Games": {},
                "Description": {},
                "Business": {},
                "Name": {},
                "Voiced": {}
            }
        },
        "size": 1000
    })

    # Вывод найденных персонажей
    for i in range(10):
        print("=========================")
        print(f'======Персонаж #{i+1}=====')
        print("=========================")
        name = response['hits']['hits'][i]['_source']['Name']
        games = response['hits']['hits'][i]['_source']['Games']
        business = response['hits']['hits'][i]['_source']['Business']
        voiced = response['hits']['hits'][i]['_source']['Voiced']
        gender = response['hits']['hits'][i]['_source']['Gender']
        nationality = response['hits']['hits'][i]['_source']['Nationality']
        state = response['hits']['hits'][i]['_source']['State']
        description = response['hits']['hits'][i]['_source']['Description']
        highlight_game = response['hits']['hits'][i].get('highlight', {}).get('Games', [])
        highlight_description = response['hits']['hits'][i].get('highlight', {}).get('Description', [])
        highlight_business = response['hits']['hits'][i].get('highlight', {}).get('Business', [])
        highlight_name = response['hits']['hits'][i].get('highlight', {}).get('Name', [])
        highlight_voiced = response['hits']['hits'][i].get('highlight', {}).get('Voiced', [])

        if name is not None:
            print("\nИмя:\n" + name)

        if games is not None:
            for item in games:
                print("\nИгра:\n" + item)
        else:
            print("\nИгра отсутствует\n")

        if business is not None:
            for item in business:
                print("\nРод деятельности:\n" + item)
        else:
            print("\nРод деятельности отсутствует\n")

        if voiced is not None:
            for item in voiced:
                print("\nОзвучен:\n" + item)
        else:
            print("\nНе озвучен\n")

        if gender is not None:
            print("\nПол:\n" + gender)
        else:
            print("\nПол отсутствует\n")

        if nationality is not None:
            print("\nНациональность:\n" + nationality)
        else:
            print("\nНациональность отсутствует\n")

        if state is not None:
            print("\nСостояние:\n" + state)
        else:
            print("\nСостояние отсутствует\n")

        if description is not None:
            print("\nОписание:\n")
            for item in description:
                print(item)
        else:
            print("\nОписание отсутствует\n")

        if highlight_name is not None:
            print("\nНайденное совпадение в имени:\n")
            print(highlight_name)
            print()
        else:
            print("\nСовпадение отсутствует\n")

        if highlight_game is not None:
            print("\nНайденное совпадение в игре:\n")
            print(highlight_game)
            print()
        else:
            print("\nСовпадение отсутствует\n")

        if highlight_description is not None:
            print("\nНайденное совпадение в описании:\n")
            print(highlight_description)
            print()
        else:
            print("\nСовпадение отсутствует\n")

        if highlight_business is not None:
            print("\nНайденное совпадение в роде деятельности:\n")
            print(highlight_business)
            print()
        else:
            print("\nСовпадение отсутствует\n")

        if highlight_voiced is not None:
            print("\nНайденное совпадение в актере озвучки:\n")
            print(highlight_voiced)
            print()
        else:
            print("\nСовпадение отсутствует\n")

