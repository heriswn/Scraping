import requests
import csv

key = input('Masukan Keyword :')
limit = input('Limit Data:')
write = csv.writer(open('eCommerce/hasil/{}.csv'.format(key), 'w', newline=''))
header = ['Nama','Harga','Terjual','Stok','Lokasi Toko','Rating']
write.writerow(header)

url = 'https://shopee.co.id/api/v4/search/search_items?'

parameter = {
'by': 'relevancy',
'keyword': key,
'limit': limit,
'newest': 0,
'order': 'desc',
'page_type': 'search',
'scenario': 'PAGE_GLOBAL_SEARCH',
'version': 2
}
count=0

r = requests.get(url, params=parameter).json()
#print(r.status_code)
produk = r['items']
for p in produk:
    nama = p['item_basic']['name']
    harga = p['item_basic']['price']
    terjual = p['item_basic']['sold']
    stok = p['item_basic']['stock']
    lokasitoko = p['item_basic']['shop_location']
    rating = p['item_basic']['item_rating']['rating_star']
    count+=1
    print('No:',count,'nama:',nama,'harga:',harga,'Terjual:',terjual,'Stok:',stok,'Lokasi Toko:',lokasitoko,'Rating:',rating)
    write = csv.writer(open('eCommerce/hasil/{}.csv'.format(key),'a',newline=''))
    data = [nama,harga,terjual,stok,lokasitoko,rating]
    write.writerow(data)