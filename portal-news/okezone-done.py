import requests
from bs4 import BeautifulSoup
import csv

key = input('Masukan Keyword :')
hal = int(input('Berapa Halaman:'))
write = csv.writer(open('portal-news/hasil/{}.csv'.format(key), 'w', newline=''))
header = ['Judul Artikel','Tanggal Upload','Alamat']
write.writerow(header)

count_page = 0
for page in range(0,hal):
    count_page+=1
    print('Scraping page: ',count_page)
    url = 'https://search.okezone.com/searchsphinx/loaddata/article/{}/{}'.format(key,page)

    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    items = soup.findAll('div','listnews')
    for item in items:
        judul = item.find('div','title').text
        upload = item.find('div','tgl').text
        url = item.find('a')['href']
        print('Judul:',judul,'Upload:',upload,'url:',url)
        write = csv.writer(open('portal-news/hasil/{}.csv'.format(key),'a',newline=''))
        data = [judul,upload,url]
        write.writerow(data)