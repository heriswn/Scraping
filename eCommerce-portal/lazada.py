import requests
from bs4 import BeautifulSoup

url = 'https://www.lazada.co.id/catalog/?q=cosmos&_keyori=ss&from=input&spm=a2o4j.home.search.go.50151559pwK831'
header = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
r = requests.get(url,headers=header)
print(r.status_code)
#produk = r['items']
#soup = BeautifulSoup(r.text,'html.parser')
#items = soup.findAll('div','index__gridItem___3VkVO')
#for item in items:
#    produk = item.find('i','ic-dynamic-badge ic-dynamic-badge-lazMall ic-dynamic-group-3')
#    harga = item.find('span','index__currency___Q78Jz')
#    print(produk,harga)