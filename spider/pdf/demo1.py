# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2022/4/3 10:43
Author : Dufy
Email : 813540660@qq.com
File : demo1.py

爬取网上操作系统书籍示例
https://www.kean.edu/~gchang/tech2920/http___professor.wiley.com_CGI-BIN_JSMPROXY_DOCUMENTDIRECTORDEV%2BDOCUMENTID%260471715425%2BDOCUMENTSUBID%261%2BPRFVALNAME%26pdfs_ch18.pdf

==============================================================================
"""

import traceback
import requests


if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36',

    }
    status_record = {}
    for ch_ind in range(-1,60):
        print(ch_ind)
        filename = f"/Users/dufy/Documents/操作系统/chap_{ch_ind}.pdf"
        url = f"https://www.kean.edu/~gchang/tech2920/http___professor.wiley.com_CGI-BIN_JSMPROXY_DOCUMENTDIRECTORDEV+DOCUMENTID&0471715425+DOCUMENTSUBID&1+PRFVALNAME&pdfs_ch{ch_ind}.pdf"  # 等价下面的
        if ch_ind<10:
            url = f"https://www.kean.edu/~gchang/tech2920/http___professor.wiley.com_CGI-BIN_JSMPROXY_DOCUMENTDIRECTORDEV+DOCUMENTID&0471715425+DOCUMENTSUBID&1+PRFVALNAME&pdfs_ch0{ch_ind}.pdf"  # 等价下面的
        print(f"请求url: {url}")
        response = requests.get(url, headers=headers)
        status_record[ch_ind] = response.status_code
        print(response.content)
        if response.status_code ==200:
            with open(filename, 'wb+') as f:
                f.write(response.content)
        print(status_record)
    print(status_record)
    print(f'done!!')
