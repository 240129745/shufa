#!/usr/bin/env python
#  
# @Version : 1.0  
# @Time    : 17-10-24  
# @Author  : su
from __future__ import unicode_literals
import requests
from bs4 import BeautifulSoup
import os
import time
import lxml
import codecs
import sys
import chardet
import urllib

url="http://www.9610.com/Index1.htm"
home="http://www.9610.com/"

def get_img(home,url):
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "lxml")
    morelist = soup.select("p > a")
    for i in morelist:
        page=i.get("href")
        if page is None:
            continue
        if "htm" in page:
            print (type(page),home+page)
        else:
            get_img(home+page)

def get_homeweb(url):
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "lxml")
    morelist = soup.select("p > a")
    for i in morelist:
        #print (url+i.get("href"))
        get_img(url,url+i.get("href"))

# web = requests.get(url)
# soup = BeautifulSoup(web.text,"lxml")
# morelist=soup.find_all("a")
#
# for m in  morelist:
#     print (home+m.get("href"))

if __name__=='__main__':
    get_homeweb("http://www.9610.com/wangxizhi/")
