import requests
from bs4 import BeautifulSoup

key = input('Masukan judul drama:')
url = 'https://oppadrama.me/?s={}'.format(key)

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
drama = soup.findAll('article','bs')
for d in drama:
    judul = d.find('h2').text
    url = d.find('a')['href']
    print(judul,url)
