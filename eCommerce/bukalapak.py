import requests
import csv

header = {
  'cookie': 'browser_id=43bdfeae32790add1f32c5d62e11ce70; identity=f7ff92f2c88c334c0f92c2bd7f7c83ac; browser_id=bd532c7168fab455f90f5ff25919ac12; session_id=94cf407ffb89b8839cda3071003f995e; lskjfewjrh34ghj23brjh234=dFRFaW5QbWdZYTVENmp2MllCMHhPbGtRSm44Vlh6M0cwSTNXNzk2aVE0ODFkQ1FzanJyVjBIWE5RajFpOS9CTzl2MU94MlUxajc2NUdsYjFHTjlwa0E9PS0teHdnUHhKcnZhOGcrNEp1cDd2MU1wZz09--01c0821cf3772c4cb6c10569f4908b256933f188; __cfruid=16f2ecb9d8511537c487cd3b414799a5ee109b8b-1625196757',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = "https://www.bukalapak.com/products?from=omnisearch&from_keyword_history=false&search%5Bkeywords%5D=bolde&search_source=omnisearch_keyword&source=navbar"
r = requests.get(url,headers=header)
print(r)