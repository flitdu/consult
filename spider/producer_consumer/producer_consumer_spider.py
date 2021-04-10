# -*- coding: utf-8 -*-
"""
@Time : 2021/3/29 9:58 下午
@Author : Dufy
@Email : 813540660@qq.com
@File : producer-consumer-spider.py
@Software: PyCharm 
Description :
1)  生产者、消费者模式爬虫
2)  参考：[【2021最新版】Python 并发编程实战，用多线程、多进程、多协程加速程序运行](https://www.bilibili.com/video/BV1bK411A7tV?p=6&spm_id_from=pageDriver)
"""
import queue
from producer_consumer import blog_crawl
import time
import random
import threading

url  ='https://www.cnblogs.com/AggSite/AggSitePostList'

def do_crawl(url_queue:queue.Queue, html_queue:queue.Queue):
    while 1:
        index = url_queue.get()
        html = blog_crawl.crawl(url, index)
        html_queue.put(html)
        print(threading.current_thread().name, f'crawl{url}',
              'url_queue.size=', url_queue.qsize())
        time.sleep(random.randint(1,2))

def do_parse(html_queue:queue.Queue, fout):
    while 1:
        html = html_queue.get()
        results = blog_crawl.parse(html)
        for result in results:
            fout.write(str(result)+'\n')
        print(threading.current_thread().name, f'results.size', len(results),
                  'html_queue.size=', html_queue.qsize())
        time.sleep(random.randint(1,2))


if __name__ == "__main__":
    pass
    url_queue = queue.Queue()
    html_queue = queue.Queue()
    for index in range(1,5):
        url_queue.put(index)
    for thread_num in range(3):  # 生产者线程
        t = threading.Thread(target=do_crawl,
                             args=(url_queue, html_queue),
                             name=f'crawl{thread_num}')
        t.start()

    fout = open('data.txt', 'w')  # 文件输出
    for thread_num in range(2): # 消费者线程
        t = threading.Thread(target=do_parse,
                             args=(html_queue, fout),
                             name=f'parse{thread_num}')
        t.start()