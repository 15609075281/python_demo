# conding=utf-8
'''
解析贝壳成都新房楼盘网页信息
获取每一个楼盘的项目名、地址、单价

使用MongDb数据库进行存储
使用csv文件进行保存
'''

import pymongo
import requests
from bs4 import BeautifulSoup
import csv
import time
import datetime

# 成都新房楼盘总入口地址
url = 'https://cd.fang.ke.com/loupan/p_xfxymdeqabenr/'
# 成都新房楼盘第二页
url_2 = 'https://cd.fang.ke.com/loupan/pg2/'

# 首页项目名地址
# worknameurl = ' li.resblock-list '
worknameurl = ' body > div.resblock-list-container.clearfix > ul.resblock-list-wrapper > li:nth-child(1) > div > div.resblock-name > a '
worknameurl_1 = ' a.name '
# 单页项目名地址
singurls = ' div.box-left-top > div > a > h1'
# 单页地址
work_address = ' p.where.manager > span'
# 单页单价
money_address = ' span.junjia'
money_address = ' span.yuan'

headers = {
    'suser-Agents': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36',
    'cookies': 'lianjia_uuid=35e4fa5e-a9fe-4e86-858b-643e2306e0fa; select_city=510100; gr_user_id=92d1beea-2b25-4ab7-9ba8-d66eacca511a; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1529390693; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1529390693; _smt_uid=5b28a664.3deb3cab; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216416c9fa89656-0193f4894b5fce-6415147f-2073600-16416c9fa8a3bd%22%2C%22%24device_id%22%3A%2216416c9fa89656-0193f4894b5fce-6415147f-2073600-16416c9fa8a3bd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Fs%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E8%B4%9D%E5%A3%B3%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22sousuo%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; gr_session_id_a1a50f141657a94e=0ff04264-6d58-486b-8801-f8ee18055273_true; lianjia_ssid=4a2f4e32-bf3b-434a-a0bd-efa64cfa200d'
}


def getRuests(url):
    print('对首页解析获取源网页')
    url = requests.post(url, headers=headers)
    soup = BeautifulSoup(url.text, 'html.parser')
    # 遍历出每一条item
    print('soup.select(worknameurl):::::%s' % soup.select(worknameurl))
    for var_soup in soup.select(worknameurl):
        print('var_soup:::::%s' % var_soup)
        # 将获得的每一个item的连接提取出来
        data1 = var_soup.select(worknameurl_1)
        data = {
            data1
        }
        print(data)
        # getRuests_one()


def getRuests_one():
    print('对单个网页解析获取源网页')
    setPyMong()
    setCsv()


def setPyMong(arr):
    print('执行mongodb存储')
    library = pymongo.MongoClient("mongodb://localhost:27017/")
    ## 数据库判断,返回集合sql
    # db_sql = getData(library)
    beike = library['beike']
    cdxf = beike['cdxf']
    # 插入字典
    x = cdxf.insert_one(arr)
    print(x)
    # # 插入列表
    # db_sql.insert_many(arr)


def setCsv():
    print('执行csv存储')


if __name__ == '__main__':
    print('开始')
    getRuests(url_2)
