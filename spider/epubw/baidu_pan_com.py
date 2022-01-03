"""
利用Python爬取epubw整站27502本高质量电子书，并自动保存至百度网盘（内附分享）
https://imyshare.com/article/23/

"""

import requests  #需要安装
import execjs    #需要安装
from tqdm import tqdm
import random, time
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


#在浏览器中打开网盘页面，抓包获取相应参数并填写在''里
headers = {'Host': 'pan.baidu.com',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',} #填写
BAIDUID = 'C56B70FCFF62989A804F051C204B6D29' #填写
STOKEN = '101d8e27b3f5d073bc7a02584db827017f8ffabc5698b09a48ff017bdebdae08' #填写
BDUSS = 'VQxM3dlYlRmUlZrZ245enVRRkNUVVdqcjZMcjlOMFZsMnVJN3ROMExxbml-ZmhoSVFBQUFBJCQAAAAAAAAAAAEAAAALujwlZHV6aGl5dWFubAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOJw0WHicNFhM' #填写
BIDUPSID = '44D0DAA4CF20F1C9F9B9766138E88E7E' #填写
csrfToken = 'HU7nevWbi2iKYm-rIfRBK8AG' #填写


session = requests.Session()
session.cookies['BDUSS'] =  BDUSS 
session.cookies['STOKEN'] = STOKEN
session.cookies['BAIDUID'] = BAIDUID
session.cookies['BIDUPSID'] = BIDUPSID 
session.cookies['csrfToken'] = csrfToken
session.mount('http://', HTTPAdapter(max_retries=3))
session.mount('https://', HTTPAdapter(max_retries=3))


#以下几个参数需要抓包目标文件夹页面的链接https://pan.baidu.com/mbox/msg/shareinfo? ，转存时候的请求才能拿到，填写在''里
from_uk='2285797942' #填写
msg_id='3084170826251150880' #填写
gid='786310019708420581' #填写
fs_id='831852965036740' #填写
app_id='250528' #填写
logid='MTY0MTEzNDgwNzM2NzAuNDI3NjA1MDYyMjY4NTA4MzY=' #填写，最后是=也正常


#这个参数填入你自己要保存的网盘路径，例如：'/电子书'，尽量确定好，以后文件太多可能改不了
path='/EPUB书库/类别' #填写

def get_logid(baidu_id):
    with open('boot.js', encoding='utf-8') as f:
        bootjs = f.read()
    js_obj = execjs.compile(bootjs)
    res = js_obj.call('getLogId', baidu_id)
    return res


def transfer_to_cloud(book_list, list_class_id):
    print(f'传至云盘.....')
    sec = random.uniform(0, 1)
    print(f'等待{sec} 秒')
    time.sleep(sec)

    logid = get_logid(BAIDUID)

    transfer_url = '/mbox/msg/transfer?web=1&logid=' + logid + '&clienttype=0&channel=chunlei'
    form_data = {
        'from_uk': from_uk,
        'msg_id': msg_id,
        'path': [path+str(i) for i in list_class_id],
        'ondup': 'newcopy',
        'async': 1,
        'type': 2,
        'gid': gid,
        'fs_ids': '[' + ','.join(str(i) for i in book_list) + ']'
    }

    headers['referer'] = 'https://pan.baidu.com/mbox/homepage'
    headers['Content-Type'] = 'application/x-www-form-urlencoded;charset=UTF-8'
    # print(form_data)
    try:
        requests.adapters.DEFAULT_RETRIES = 3
        # response = requests.post(url, data=body, headers=http_headers, timeout=5)
        save_res = session.post('https://pan.baidu.com' + transfer_url,
                                headers=headers,
                                data=form_data,
                                # timeout=5
                                )
    except Exception as ee:
        print(ee)
    # save_res = session.post('https://pan.baidu.com' + transfer_url,
    #                         headers=headers,
    #                         data=form_data,
    #                         )
    save_json = save_res.json()
    print(save_json)
    print(f'传至云盘结束')


def get_pan_list(page, f):
    headers['Host'] = 'pan.baidu.com'
    url = 'https://pan.baidu.com/mbox/msg/shareinfo?msg_id='+str(msg_id)+'&from_uk='+str(from_uk)+'&gid='+str(gid)+'&type=2&fs_id='+str(fs_id)+'&cursor=&page=' + str(
        page) + '&num=50&bdstoken='+'&channel=chunlei&web=1&app_id='+str(app_id)+'&logid='+logid+'&clienttype=0'
    # print(str(url))
    list_res = session.get(url, headers=headers)
    list_josn = list_res.json()
    print(f'请求内容如下：')
    class_id = []  # 类目id
    for i in list_josn['records']:
        name_i = f'类别：{i["category"]}--《{i["server_filename"][15:]}》'
        print(name_i)
        class_id.append(i['category'])
        f.write(name_i+'\n')
    # print(list_josn)
    fid = []
    for item in list_josn['records']:
        fid.append(item['fs_id'])
    # print('长度：', len(fid))
    return fid, class_id


def run():
    f = open('epubw_book_names.txt', 'a+', encoding='utf8')
    all_num = 0
    for n in tqdm(range(3000)):
    # for n in range(1, 3):   #页面可选， 3000
        if n<=550: continue
        print(f'---'*30)
        print('正在请求第' + str(n) + '页')
        list_b, list_class_id = get_pan_list(n,f)
        print('正在保存第' + str(n) + '页')
        all_num += len(list_b)
        print(f'已保存：{all_num} 份')
        if len(list_b) >0:
            transfer_to_cloud(list_b, list_class_id)
        else:
            print('已经到底了')
            break

run()   #报错也没关系



