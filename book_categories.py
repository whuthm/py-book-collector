# -*- coding: utf-8 -*-

"""
    Created by huangming on 03/02/2018.
"""

import utils

_key = 'book_categories'


def getcategories():
    try:
        soup = utils.fetch_page('http://www.yousuu.com')
        categories = []
        for tag in soup.find_all(attrs={"class": "col-md-1 col-sm-2 col-lg-1 col-xs-2"}):
            if tag.a['href'].startswith('/category/'):
                cate_key = tag.a['href'].replace('/category/', '')
                cate_name = tag.a.string
                category = {"key": cate_key, "name": cate_name}
                categories.append(category)
        return categories
    except Exception as e:
        print(e)
        return ''


if __name__ == '__main__':
    if not '':
        print('\'\' is false')

    if not []:
        print('[] is false')

    if not None:
        print('None is false')

    categories = getcategories()
    if categories:
        utils.save_data_json_to_local(_key, categories)
