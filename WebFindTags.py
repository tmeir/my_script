import requests
from bs4 import BeautifulSoup

try:
    url = input("Enter URL: ")
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0'}
    req = requests.get(url, headers= headers )
    page = BeautifulSoup(req.text,'html.parser')
    print(page.prettify())
    print("===============================================================================================")

    find_tag = input("Enter tag to find: ")

    soup4 = page.find_all(find_tag)
    for line in soup4:
        print(line)
except Exception as e:
    print(e)