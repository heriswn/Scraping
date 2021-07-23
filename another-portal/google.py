import requests
from bs4 import BeautifulSoup

def response_info(r,*args,**kwargs):
    print(r.status_code)
    #print(r.text)

def response_headers(r,*args,**kwargs):
    print(r.headers)

hooks = {'response': (response_info)}
r = requests.get('https://www.google.com/search?q=liverpool&source=hp&ei=zFXlYPifPPm-3LUP94CluAk&iflsig=AINFCbYAAAAAYOVj3ToJn49MqG-XC7v1715yZY1Qphac&oq=liverpool&gs_lcp=Cgdnd3Mtd2l6EAMyCAguELEDEJMCMgIIADICCAAyCAgAELEDEIMBMggIABCxAxCDATICCAAyAggAMgIIADICCAAyCAgAELEDEIMBOgUIABCxAzoCCC46CAguELEDEIMBOggIABCxAxCLA1DX_EtYz4xMYIKPTGgDcAB4AIABowGIAbQJkgEDMC45mAEAoAEBqgEHZ3dzLXdperABALgBAg&sclient=gws-wiz&ved=0ahUKEwj4tdyDttDxAhV5H7cAHXdACZcQ4dUDCAY&uact=5',hooks=hooks)
soup = BeautifulSoup(r.text,'html.parser')
items = soup.findAll('div','g')
for item in items:
    judul = item.find('h3','LC20lb DKV0Md').text
    url = item.find('a')['href']
    print(judul,url)