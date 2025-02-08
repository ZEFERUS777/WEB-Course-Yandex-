import requests
from bs4 import BeautifulSoup


html = requests.request(
    method = 'GET',
    url = 'https://briefly.ru/lermontov/mcyri/'
).content.decode('utf-8')
output = []
search = r'<img[^>]+src="([^">]+)"'
soup = BeautifulSoup(html, 'html.parser')
for img in soup.find_all('p', class_='microsummary__content'):
    text = img.text.split()
    for symbol in text:
        if '.' in symbol:
            output.append(symbol+'\n')
        else:
            output.append(symbol)
print(' '.join(output))