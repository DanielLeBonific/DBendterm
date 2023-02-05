import requests
from bs4 import BeautifulSoup

pages = range(1, 37)
data = []
for page in pages:
    url = f"http://kiz0dar-ctf.ru/prostitutki/astany/{page}"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    girls = soup.find_all(class_="box profilebox")

    for girl in girls:
        girl_name = girl.find('span', class_='name h3')
        girl_phone = girl.find('a', class_='tel')
        info_spans = girl.find_all('span', {'class': 'grey'})
        info1 = info_spans[0].text.strip()
        info2 = info_spans[1].text.strip()
        info3 = info_spans[2].text.strip()
        info4 = info_spans[3].text.strip()
        info5 = info_spans[4].text.strip()
        info6 = info_spans[5].text.strip()

        print(f"Имя: {girl_name.text.strip()}")
        print(f"Номер: {girl_phone.text.strip() }")
        print(f"Рост: {info1}")
        print(f"Вес: {info2}")
        print(f"Грудь: {info3}")
        print(f"Возраст: {info4}")
        print(f"Нация: {info5}")
        print(f"Город: {info6}")

        print('')

