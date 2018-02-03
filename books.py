# -*- coding: utf-8 -*-

"""
    Created by huangming on 03/02/2018.
"""

import utils
import re

_key = 'books'



def get_page_count():
    page_count = 0
    try:
        soup = utils.fetch_page('http://www.yousuu.com/category/all')
        page_indicator = soup.find(attrs={'class', 'books'}).ul.children
        for indicator_item in page_indicator:
            try:
                onclick = indicator_item.a['onclick']
                page_count = max(page_count, int(str(onclick).split(',')[1].replace(')', '').replace('\'', '')))
            except Exception as e:
                print(e)

            print(indicator_item)
    except Exception as e:
        print(e)
    return max(1, page_count)


def getbooks():
    books = []
    #page_count = get_page_count()
    page_count = 1
    for page in range(1, page_count + 1):
        get_books_from(books, page)
    return books

def get_books_from(books, page):
    try:
        soup = utils.fetch_page('http://www.yousuu.com/category/all?page={}'.format(page))
        for book_subject in soup.find_all(attrs={'class', 'bd booklist-subject'}):
            book = {}
            for div in book_subject.children:
                if div['class'] == 'pull-right hidden-xs btn-group initshelf'.split(' '):
                    book['id'] = div['data-bid']
                elif div['class'] == ['post']:
                    book['cover'] = div.a.img['src']
                elif div['class'] == ['title']:
                    book['name'] = div.a.string
                elif div['class'] == ['rating']:
                    # 评分的人数
                    book['rating_num'] = int(re.findall('\d+', re.findall(r'(\d+人评价)', str(div))[0])[0])
                elif div['class'] == ['abstract']:
                    book['rating'] = float(div.span.string)
                    # 贪婪匹配，使用* 或者 + 时都是匹配最长的字符串，加一个?则可以匹配最短的字符串
                    author_name_line = re.findall(r'作者:\s[\s\S]*?<br/>', str(div))[0]
                    # 去除头和尾部，使用sub函数替换
                    book['author_name'] = re.sub(r'作者:\s|<br/>', '', author_name_line)
                    word_num_line = re.findall(r'字数:\s[\s\S]*?<br/>', str(div))[0]
                    book['word_num'] = re.sub(r'字数:\s|<br/>', '', word_num_line).strip()
                    updated_time_line = re.findall(r'最后更新:\s[\s\S]*?<br/>', str(div))[0]
                    book['updated_time'] = re.sub(r'最后更新:\s|<br/>', '', updated_time_line).strip()

            books.append(book)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # books = getbooks()
    # if books:
    #     utils.save_data_json_to_local(_key, books)
    page_count = get_page_count()
    print('Total page count: %d' % page_count)
    #page_count = 1
    for page in range(1, page_count + 1):
        print('---fetch book page %d---' % page)
        books = []
        get_books_from(books, page)
        utils.save_data_json_to_local('{}_page{}'.format(_key, page), books)
        print('fetch book page %d end' % page)