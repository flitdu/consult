# -*- coding: utf-8 -*-
"""
==============================================================================
Time : 2021/7/17 5:31 下午
Author : Dufy
Email : 813540660@qq.com
File : bom_segmentation.py

特殊例子：
[
'L10;4u7;Taiyo Yuden;NRG4026T4R7M;INDUCTOR 4.7UH 1.6A 20% SMD',
'26 贴片电感 3.9NH/10% 0402_1/16W 1 L3 4000.0',
'r372b002lt300 NJ2LT30039 IHLP2525CZER4R7M11/IHLP PRODUCT FAMILY/4.7uH/±20% Vishay 电感 IHLP2525CZER4R7M11/IHLP PRODUCT FAMILY/4.7uH/±20% L2 1 PCS',
'6 贴片电感   10uH   3A MDH6045C-100MB=P3 6*6.3MM 15 Murata',
'HUNAN CHAMPIONS CET0315-4R7M IND,4.7UH,+/-20%,1.9A,220mOhm,CET0315-4R7M,G 105',


]

关于bom 分词的一些尝试
==============================================================================
"""


import traceback
import pandas as pd
import json
import re
from utils import remove_nan_string, datapath
import jieba
jieba.load_userdict(datapath('data/dict.txt'))

# re_han = re.compile("([ \u4E00 - \u9FD5 a-zA-Z0-9+#&\._%\-]+)" , re.U)
re_han = re.compile("([ \u4E00-\u9FD5;]+)", re.U)
df = pd.read_csv('/Users/dufy/code/corpus/para.txt', sep='@@', header=None)
para_dict = {v:k for k,v in df[0].to_dict().items()}


if __name__ == "__main__":
    pass
    path = r'/Users/dufy/code/corpus/bom0526.xls'
    save_path = datapath('data/record.txt')
    df = pd.read_excel(path)
    print(df.info())
    print(df.head())
    print(df.iterrows())

    f = open(save_path,'w', encoding='utf8')
    for ind, row in df[:4000].iterrows():
        print('-'*30)
        origin_content = row['row_content']
        print(f'原始bom输入:{origin_content}')
        origin_split = re_han.split(origin_content.lower())
        print(f'原始分割：{origin_split}')
        tmp = []
        for block in origin_split:
            flag = True
            # print(f'block: {block}')
            block = block.strip().strip('()（）;,:：')
            # print(f'block: {block}')
            if not block: continue
            if re_han.match(block):
                tmp += list(jieba.cut(block))
            else:
                if bool(re.search(r'\b\d+/\d+ *w\b', block)):  # 1/8w 情况
                    para_list1 = re.split("\(|、|，|,|；", block)
                    para_list2 = re.split("\(|、|，|_|；", block)
                    para_list3 = re.split("\(|、|，|-|；", block)
                    para_list4=[]
                else:
                    para_list1 = re.split('\(|、|，|,|；', block)
                    para_list2 = re.split('\(|、|，|_|；', block)
                    para_list3 = re.split('\(|、|，|-|；', block)
                    para_list4 = re.split('\(|、|，|/|／|；', block)
                len_dic = {0:para_list1, 1:para_list2, 2:para_list3, 3:para_list4}
                len_list = [len(i) for i in len_dic.values()]
                max_index = len_list.index(max(len_list))  #长度最大对应的索引
                para_list = len_dic[max_index]
                    
                print(f'参数初始分割：{para_list}')
                if len(para_list)==1: tmp += para_list
                else:
                    for i in para_list:
                        if i in para_dict or not i.strip():
                            pass
                        else:  # 说明不是参数组合
                            tmp.append(block)
                            flag=False
                            break
                    if flag:
                        tmp += para_list
        tmp = remove_nan_string(tmp)

        f.write('-'*20+'\n')
        f.write(origin_content+'\n')
        f.write(' '.join(tmp)+'\n')

        print(tmp)