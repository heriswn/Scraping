import requests
import csv

key=input('Masukan produk yang akan dicari:')
limit=input('Masukan limit produk:')
hal = input('Masukan berapa halaman ke berapa:')

write = csv.writer(open('eCommerce/hasil/{}.csv'.format(key), 'w', newline=''))
header = ['nama produk','harga','terjual','rating produk','nama toko','lokasi toko']
write.writerow(header)

header = {
  'authority': 'gql.tokopedia.com',
  'method': 'POST',
  'path': '/',
  'scheme': 'https',
  'accept': '*/*',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'en-US,en;q=0.9,id;q=0.8',
  'content-length': '3091',
  'content-type': 'application/json',
  'origin': 'https://www.tokopedia.com',
  'referer': 'https://www.tokopedia.com/search?st=product&q={}&navsource=home'.format(key),
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

data = {
  "operationName": "SearchProductQueryV4",
  "variables": {
    "params": "device=desktop&navsource=home&ob=23&page={}&q={}&related=true&rows={}&safe_search=false&scheme=https&shipping=&source=search&st=product&start=0&topads_bucket=true&unique_id=bcff84691771dfbce6b4a85ee24ff652&user_addressId=&user_cityId=176&user_districtId=2274&user_id=&user_lat=&user_long=&user_postCode=&variants=".format(hal,key,limit)
  },
  "query": "query SearchProductQueryV4($params: String!) {\n  ace_search_product_v4(params: $params) {\n    header {\n      totalData\n      totalDataText\n      processTime\n      responseCode\n      errorMessage\n      additionalParams\n      keywordProcess\n      __typename\n    }\n    data {\n      isQuerySafe\n      ticker {\n        text\n        query\n        typeId\n        __typename\n      }\n      redirection {\n        redirectUrl\n        departmentId\n        __typename\n      }\n      related {\n        relatedKeyword\n        otherRelated {\n          keyword\n          url\n          product {\n            id\n            name\n            price\n            imageUrl\n            rating\n            countReview\n            url\n            priceStr\n            wishlist\n            shop {\n              city\n              isOfficial\n              isPowerBadge\n              __typename\n            }\n            ads {\n              adsId: id\n              productClickUrl\n              productWishlistUrl\n              shopClickUrl\n              productViewUrl\n              __typename\n            }\n            badges {\n              title\n              imageUrl\n              show\n              __typename\n            }\n            ratingAverage\n            labelGroups {\n              position\n              type\n              title\n              __typename\n            }\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      suggestion {\n        currentKeyword\n        suggestion\n        suggestionCount\n        instead\n        insteadCount\n        query\n        text\n        __typename\n      }\n      products {\n        id\n        name\n        ads {\n          adsId: id\n          productClickUrl\n          productWishlistUrl\n          productViewUrl\n          __typename\n        }\n        badges {\n          title\n          imageUrl\n          show\n          __typename\n        }\n        category: departmentId\n        categoryBreadcrumb\n        categoryId\n        categoryName\n        countReview\n        discountPercentage\n        gaKey\n        imageUrl\n        labelGroups {\n          position\n          title\n          type\n          __typename\n        }\n        originalPrice\n        price\n        priceRange\n        rating\n        ratingAverage\n        shop {\n          id\n          name\n          url\n          city\n          isOfficial\n          isPowerBadge\n          __typename\n        }\n        url\n        wishlist\n        sourceEngine: source_engine\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n"
}

url = "https://gql.tokopedia.com/"
response = requests.post(url, headers=header, json=data)
res_json = response.json()

produk = res_json['data']['ace_search_product_v4']['data']['products']
for p in produk:
    nama = p['name']
    harga = p['price']
    terjual = p['labelGroups'][0]['title']
    rating = p['ratingAverage']
    nama_toko = p['shop']['name']
    lokasi_toko = p['shop']['city']
    print('nama produk:',nama,'harga:',harga,'terjual:',terjual,'rating produk:',rating,'nama toko:',nama_toko,'lokasi toko:',lokasi_toko)
    write = csv.writer(open('eCommerce/hasil/{}.csv'.format(key),'a',newline=''))
    data = [nama,harga,terjual,rating,nama_toko,lokasi_toko]
    write.writerow(data)