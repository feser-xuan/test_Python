# -*- coding:utf-8 -*-
# @author: Weixuan.Ding
# @time  : 2018/12/17 14:11
# @E-mail：weixuanfeser@gmail.com
# @Software: PyCharm
import re
from bs4 import BeautifulSoup
import requests
from docx import Document
import sys
import os
def main():
    print(os.path.exists('demo.docx'))
    url = 'https://www.liuxue86.com/a/2635898.html'
    r = requests.get(url)
    # print(r.text, '\n{}\n'.format('*' * 79), r.encoding)
    url_encoding = re.findall(re.compile(r'charset="\S*"'), r.text)
    if len(url_encoding):
        r.encoding = url_encoding[0].split('"')[1]
    # print(r.text, '\n{}\n'.format('*' * 79), r.encoding)
    if os.path.exists('demo.docx'):
        os.remove('demo.docx')
        print('remove demo.docx success!')
    doc = Document()
    print([s.name for s in doc.styles if s.type == 1])
    soup = BeautifulSoup(r.text,'html.parser')
    print(re.findall(re.compile(r'charset="\S*"'),r.text))
    for p in soup.find_all('p'):
        if p.string is None:
            continue
        else:
            doc.add_paragraph(p.string,style='Body Text')
            print(p.string)
    # p_node = soup.find('p',class_='content')
    # print(p_node)
    doc.save('demo.docx')
if __name__ == '__main__':
    main()



