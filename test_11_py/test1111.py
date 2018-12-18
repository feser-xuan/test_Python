# -*- coding:utf-8 -*-
# @author: Weixuan.Ding
# @time  : 2018/11/11 19:47
# @E-mail：weixuanfeser@gmail.com
# @Software: PyCharm

# 爬虫练习
#
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# import re
# import random
#
# base_url = 'https://baike.baidu.com'
# his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]
# for i in range(20):
#     url = base_url + his[-1]
#
#     html = urlopen(url).read().decode('utf-8')
#     soup = BeautifulSoup(html,features='lxml')
#     print(soup.find('h1').get_text(),'url:',his[-1])
#
#     sub_urls = soup.find_all('a',{'target':'_blank','href':re.compile('/item/(%.{2})+$')})
#
#     if len(sub_urls) != 0:
#         his.append(random.sample(sub_urls,1)[0]['href'])
#     else:
#         his.pop()
#
#     # print(his)

# requests 请求

import requests
import webbrowser

param = {"wd":"莫烦python"}
r = requests.get('http://www.baidu.com/s', params=param)
# requests.post()
print(r.url)
webbrowser.open(r.url)
# import requests
# import webbrowser
# param = {"wd": "莫烦Python"}  # 搜索的信息
# r = requests.get('http://www.baidu.com/s', params=param)
# print(r.url)
# webbrowser.open(r.url)



