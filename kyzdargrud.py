import pandas as pd
import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

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

        girl_data = {
            'name': girl_name.text.strip(),
            'phone': girl_phone.text.strip(),
            'info1': info1,
            'info2': info2,
            'info3': info3,
            'info4': info4,
            'info5': info5,
            'info6': info6
        }
        data.append(girl_data)

df = pd.DataFrame(data)

author_counts = df['info3'].value_counts()

print(author_counts)

plt.figure(figsize=(12,6))
author_counts[:10].plot(kind='bar')
plt.xlabel('Девушки')
plt.ylabel('Размер')
plt.title('Размер груди среди ночных бабочек')
plt.show()
