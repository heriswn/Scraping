from bs4.element import PageElement
import requests
from bs4 import BeautifulSoup

page = int(input('Masukan halaman berapa:'))
url = 'https://store.cosmos.id/peralatan-rumah?p={}'.format(page)

r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
produk = soup.findAll('li','item product product-item card border-0 shadow-sm')
for p in produk:
    nama = p.find('a','product-item-link ellipsis-title font-weight-bold').text
    harga = p.find('span','price').text
    url = p.find('a','product-item-link ellipsis-title font-weight-bold')['href']
    print('nama_produk:',nama,'harga:',harga,'alamat:',url)