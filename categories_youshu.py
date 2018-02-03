import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.yousuu.com')


soup = BeautifulSoup(r.text, 'lxml')
for tag in soup.find_all(attrs={"class": "col-md-1 col-sm-2 col-lg-1 col-xs-2"}):
    if tag.a['href'].startswith('/category/'):
        category_id = tag.a['href'].replace('/category/', '')
        category_name = tag.a.string
        print('%s: %s' % (category_id, category_name))
