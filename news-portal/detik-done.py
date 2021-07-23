import requests
from bs4 import BeautifulSoup
import csv

key = input('Masukan Keyword :')
hal = int(input('Berapa Halaman:'))
write = csv.writer(open('portal-news/hasil/{}.csv'.format(key), 'w', newline=''))
header = ['Judul Artikel','Tanggal Upload','Alamat']
write.writerow(header)

count_page = 0
for page in range(1,hal):
    count_page+=1
    print('Scraping page: ',count_page)
    url = 'https://www.detik.com/search/searchall?query={}&siteid=2&sortby=time&page={}'.format(key,page)

    r = requests.get(url+str(page))
    soup = BeautifulSoup(r.text,'html.parser')
    items = soup.findAll('article')
    for item in items:
        judul = item.find('h2','title').text
        date = item.find('span','date').text
        url = item.find('a')['href']
        print('Judul',judul,'tanggal',date,'url',url)
        write = csv.writer(open('portal-news/hasil/{}.csv'.format(key),'a',newline=''))
        data = [judul,date,url]
        write.writerow(data)
