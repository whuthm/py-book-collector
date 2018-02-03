# -*- coding: utf-8 -*-

"""
    Created by huangming on 03/02/2018.
"""

import re

print(re.findall('\d+', re.findall(r'(\d+人评价)', '(1人评价)ddd')[0])[0])
list1 = []
list1.append('post')
print(list1)

print(re.findall(r'作者:\s[\s\S]*?<br>字数', str('<div class="abstract">作者: 无风逐浪<br>字数: 77.68万<br>最后更新: 5 个月前<br>字数综合评分: <span class="num2star">0.0</span></div>')))