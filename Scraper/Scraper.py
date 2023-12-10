import requests
from bs4 import BeautifulSoup
import json

base_url = "https://gta.fandom.com/ru/wiki/Категория:Персонажи"
url = base_url
domen = "https://gta.fandom.com"
# all_person_dict = {}
#
# while True:
#     req = requests.get(url)
#     src = req.text
#     soup = BeautifulSoup(src, 'html.parser')
#     links_person = soup.find_all(class_="category-page__member-link")
#
#     for item in links_person:
#         item_text = item.text
#         item_href = domen + item.get("href")
#         print(f"{item_text}: {item_href}")
#         all_person_dict[item_text] = item_href
#
#     next_link = soup.find(class_="category-page__pagination-next wds-button wds-is-secondary")
#     if next_link:
#        url = next_link.get("href")
#        print(url)
#     else:
#       break
#
# with open("all_person_dict.json", "w", encoding="utf-8") as file:
#     json.dump(all_person_dict, file, indent=4, ensure_ascii=False)

# ------------------------------------------------

with open("all_person_dict.json", encoding="utf-8") as file:
    all_person = json.load(file)

data_list = []
for person_name, person_href in all_person.items():
    req = requests.get(url=person_href)
    src = req.text

    soup = BeautifulSoup(src, 'html.parser')
    # записываем имя
    appearance = soup.find('div', {'data-source': 'игры'})
    gender = soup.find('div', {'data-source': 'пол'})
    business = soup.find('div', {'data-source': 'бизнес'})
    voiced = soup.find('div', {'data-source': 'голос'})
    nationality = soup.find('div', {'data-source': 'национальность'})
    alive = soup.find('div', {'data-source': 'положение'})
    description = soup.find(class_="mw-parser-output").find_all(lambda tag: tag.name == 'p' and not tag.find('aside') and not tag.find_parent('p'))

    data = {}
    data["Name"] = person_name
    data["Games"] = []
    data["Business"] = []
    data["Voiced"] = []
    data["Gender"] = ""
    data["Nationality"] = ""
    data["State"] = ""
    data["Description"] = []

    print("имя: " + person_name)
    if person_name != "DB-P" and person_name != "Love Fist":
        if appearance:
            game = appearance.find('div')
            games = game.find_all('a')
            for item in games:
                 #print("появление: " + item.text)
                 data["Games"].append(item.text)
            appearance.clear()

        if gender:
            genderText = gender.find('div').text
            #print("пол: " + genderText)
            data["Gender"] = genderText
            gender.clear()

        if business:
            businessForm = business.find('div')
            businessAll_a = businessForm.find_all('a')
            for item in businessAll_a:
                #print("род деятельности: " + item.text)
                data["Business"].append(item.text)

            businessAll_li = businessForm.find_all('li')
            for item in businessAll_li:
                #print("род деятельности: " + item.text)
                data["Business"].append(item.text)

            if not businessAll_a and not businessAll_li:
                for item in businessForm:
                    #print("род деятельности: " + item.text)
                    data["Business"].append(item.text)
            businessAll_a.clear()
            businessAll_li.clear()

            business.clear()

        if voiced:
            voicedForm = voiced.find('div')
            voicedAll_a = voicedForm.find_all('a')
            for item in voicedAll_a:
                #print("озвучен: " + item.text)
                data["Voiced"].append(item.text)

            voicedAll_li = voicedForm.find_all('li')
            for item in voicedAll_li:
                #print("озвучен: " + item.text)
                data["Voiced"].append(item.text)

            if not voicedAll_a and not voicedAll_li:
                for item in voicedForm:
                    #print("озвучен: " + item.text)
                    data["Voiced"].append(item.text)
            voicedAll_a.clear()
            voicedAll_li.clear()

            voiced.clear()

        if nationality:
            nationalityText = nationality.find('div').text
            #print("национальность: " + nationalityText)
            data["Nationality"] = nationalityText
            nationality.clear()

        if alive:
            aliveText = alive.find('div').text
            #print("положение: " + aliveText)
            data["State"] = aliveText
            alive.clear()

        if description:
            for item in description:
                data["Description"].append(item.text)
                #print(item.text)

        data_list.append(data.copy())
        data.clear()

        print()

print(data_list)

with open('person.json', 'a', encoding="utf-8") as file:
    json.dump(data_list, file, indent=4, ensure_ascii=False)



