import requests
import csv

url = 'https://www.blibli.com/backend/search/products?'
parameter = {
'sort':'', 
'page': '1',
'start': '0',
'searchTerm': 'bolde',
'intent': 'true',
'merchantSearch': 'true',
'multiCategory': 'true',
'customUrl':'', 
'&'
'channelId': 'mobile-web',
'showFacet': 'false',
'userIdentifier': 'undefined',
'isMobileBCA': 'false'
}

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

r = requests.get(url,params=parameter).json()
print(r)