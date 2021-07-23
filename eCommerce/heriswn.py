import requests
from bs4 import BeautifulSoup

url = 'https://heriswn.netlify.app/'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
items = soup.findAll('article')
count = 0
for item in items:
    nama = item.find('a').text
    upload = item.find('small').text
    deskripsi = item.find('p').text
    count+=1
    print('No:',count,'Judul:',nama,'Upload:',upload,'Deskripsi:',deskripsi)