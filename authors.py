import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import json

pages = range(1, 203)  # change the range to however many pages you want to scrape
data = []
for page in pages:
    html_text = requests.get(f'https://kitap.kz/book?page={page}').text
    soup = BeautifulSoup(html_text, 'html.parser')
    books = soup.find_all('div', class_='book-item__block swiper-slide')
    for book in books:
        book_name = book.find('a', class_='book-item__name').text.strip()
        author_name = book.find('p', class_='book-item__author').text.replace(' ', '').strip()

        data.append({
            'Book Name': book_name,
            'Author Name': author_name
        })

# create a dataframe from the scraped data
df = pd.DataFrame(data)

# count number of books written by each author
author_counts = df['Author Name'].value_counts()

# print the results
print(author_counts)

plt.figure(figsize=(12,6))
author_counts[:10].plot(kind='bar')  # show only the top 10 authors
plt.xlabel('Author')
plt.ylabel('Number of books')
plt.title('Number of books written by each author')
plt.show()
