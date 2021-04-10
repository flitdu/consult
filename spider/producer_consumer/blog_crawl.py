# -*- coding: utf-8 -*-
"""
@Time : 2021/3/28 7:07 下午
@Author : Dufy
@Email : 813540660@qq.com
@File : blog_crawl.py
@Software: PyCharm 
Description :
1) 基础版本展示
2) post 方法 抓包
"""

import threading
import time
import requests
from bs4 import BeautifulSoup
import json


# payload = {"CategoryType":"SiteHome","ParentCategoryId":0,"CategoryId":808,"PageIndex":3,"TotalPostCount":4000,"ItemListActionName":"AggSitePostList"}
header = {'accept': 'text/plain, */*; q=0.01',
          'accept-encoding': 'gzip, deflate, br',
          'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
          'content-type': 'application/json; charset=UTF-8',
          'origin': 'https://www.cnblogs.com',
          'referer': 'https://www.cnblogs.com/',
          'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82, Safari/537.36',
          'x-requested-with': 'XMLHttpRequest'}
def crawl(url, page_index):
    r= requests.post(url,
                     data = json.dumps({"CategoryType":"SiteHome","ParentCategoryId":0,"CategoryId":808,"PageIndex":page_index,"TotalPostCount":4000,"ItemListActionName":"AggSitePostList"}),
                     headers = header)
    # print(r.text)
    return r.text

def parse(html):
    # class ="post-item-title"
    soup =  BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_ ="post-item-title")
    return [(link['href'], link.get_text())for link in links]


if __name__ == "__main__":
    page_index = 4
    for result in parse(crawl('https://www.cnblogs.com/AggSite/AggSitePostList', page_index)):
        print(result)
