# Find <!-- "xxxxxx" --->

import requests
from bs4 import BeautifulSoup
from bs4 import Comment

try:
    url = input("Enter URL: ")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'}
    req = requests.get(url,headers= headers)
    page = BeautifulSoup(req.text,'html.parser')
    print(page.prettify())
    comments = page.find_all(string=lambda text: isinstance(text,Comment))
    for c in comments:
        print(c)
        print("====================================================")
        c.extract()


except Exception as e:
    print(e)



