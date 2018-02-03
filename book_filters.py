# -*- coding: utf-8 -*-

"""
    Created by huangming on 03/02/2018.
"""

import utils

_key = 'book_filters'


def getfilters():
    filters = []
    try:
        soup = utils.fetch_page('http://www.yousuu.com/category/all')

        # tag = soup.find(attrs={'class', 'col-sm-9 col-md-10 col-lg-10 col-xs-12'})
        table = soup.find(attrs={'class', 'list'}).table
        for tr in table.children:
            td = tr.td

            id = td['id']
            if id.startswith('category_'):
                filter_item = {}
                key = id.replace('category_', '')
                print(key)
                filter_item['key'] = key
                value_entries = []
                for child in td.children:
                    if child.name == 'small':
                        filter_item['name'] = child.string
                    elif child.name == 'button':
                        value_entry = {}
                        value_entry['name'] = str(child.string).strip()
                        onclick = child['onclick']
                        value_entry['value'] = str(onclick).split(',')[1].replace(')', '').replace('\'', '')
                        value_entries.append(value_entry)
                filter_item['value_entries'] = value_entries
                filters.append(filter_item)

        # sort
        # sort_tag = soup.find(attrs={'id', 'category_sort'}) 无效
        sort_tag = soup.find(id='category_sort')
        print(sort_tag)
        sort_filter_item = {}
        sort_filter_item['key'] = 'sort'
        sort_filter_item['name'] = '排序'
        value_entries = []
        for li in sort_tag.children:
            value_entry = {}
            value_entry['name'] = str(li.a.string).strip()
            onclick = li.a['onclick']
            value_entry['value'] = str(onclick).split(',')[1].replace(')', '').replace('\'', '')
            value_entries.append(value_entry)
        sort_filter_item['value_entries'] = value_entries
        filters.append(sort_filter_item)
        print(filters)
    except Exception as e:
        print(e)

    return filters


if __name__ == '__main__':
    filters = getfilters()
    if filters:
        utils.save_data_json_to_local(_key, filters)
