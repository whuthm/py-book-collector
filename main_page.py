import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.yousuu.com')


soup = BeautifulSoup(r.text, 'lxml')
print(soup.title)