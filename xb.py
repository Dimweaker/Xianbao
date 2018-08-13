#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import chardet #字符集检测
from urllib.request import urlopen
web={1:['https://www.iqshw.com/post/new_100/index%s%s.html','https://www.iqshw.com','_'],2:['https://www.xianbaozhijia.cn/index.php/category-1%s%s.html','','_'],3:['http://www.zuanke8.com/forum-19%s%s.html','','-'],4:['http://www.xianbao5.com/sitemap2.php','','']}
#1.爱Q生活网，最多两页
#2.线报之家
#3.赚客吧
#4.线报屋，一页，网站不稳定
def coding(url):
    html = urlopen(url).read()
    encoding=chardet.detect(html)
    return encoding
def create(kind=1,page=1):
    if kind==1 and page==1:
        return [web[kind][0]%('',''),web[kind][1]]
    elif kind==1 and page>2:
        return None
    elif kind==4 and page==1:
        return [web[kind][0],web[kind][1]]
    elif kind==4 and page>1:
        return None
    else:
        return [web[kind][0]%(web[kind][2],str(page)),web[kind][1]]
def get(url,kind):
    text = requests.get(url)
    text.encoding = 'GBK' if kind==3 else 'GB2313'
    print(text.text)
    return text.text
    #获取网站源码
def find(text,kind=1):
    word='s xst' if kind==1 else 'title'
    soup = BeautifulSoup(text, 'html.parser')
    return [x for x in soup.find_all('a') if word in str(x) and 'html' in str(x)]
    #获取相关源码行
def arrange(list=[],aurl=''):
    return['活动：' + str(x.string) + '    链接：' + aurl + x.get('href') + '\n' for x in list]
def write(list=[],url='xianbao1.txt'):
    f = open(url, 'r+',encoding='utf-8')
    txt = f.read()
    f.seek(0,0)
    for word in list:
        if word not in txt:
            f.write(word)
    f.close()
    print('Finish.')
def go(kind=1,page=1):
    write(arrange(find(get(create(kind,page)[0],kind),kind),create(kind,page)[1]))
#线报保存的TXT，第3种为ANSI，其余为UTF-8
go(1)
go(2)
go(3)#请另开以ANSI为编码的TXT保存
go(4)



















































