import requests
from bs4 import BeautifulSoup
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
        book_link = book.find('a', class_='book-item__name')['href']

        data.append({
            'Book': book_name,
            'Author': author_name,
            'Link': book_link

        })

with open('books.json', 'w') as f:
    json.dump(data, f)

