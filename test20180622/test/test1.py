# coding=utf-8

import pymongo
import requests
from bs4 import BeautifulSoup
import csv
import time
import datetime
import os

one_url = ['https://www.atobo.com.cn/Companys/s-p26-y{}/'.format(str(i)) for i in range(2, 100)]

one_title_url = '#setcolor_area > div.product_contextlist.bplist > ul > li'
one_href_url = ' div > ul > li.p_name > div > ul > li.pp_name > a.CompanyName'


# mongodb数据库
def set_mongo(href):
    print()
    my = pymongo.MongoClient('localhost', 27017)
    test = my['login']
    login = test['login']
    data = {
        'href': href
    }
    login.insert_one(data)
    print(data)


def get_url():
    arr = []
    for url in one_url:
        time.sleep(5)
        url1 = requests.get(url)
        soup = BeautifulSoup(url1.text, 'html.parser')
        for var_1 in soup.select(one_title_url):
            for var_2 in var_1.select(one_href_url):
                href = var_2.get('href')
                hh = 'https:%s' % href
                data_d = (
                    hh
                )
                arr.append(data_d)
                set_name_phone(set_data_time('href'), data_d)


# 设置文件生成时间
def set_data_time(st):
    time_ = time.localtime(time.time())
    data_day = datetime.date.today()
    folder = 'E:\sc\四川%s-%s点%s.csv' % (data_day, time_.tm_hour, st)
    return folder


# 存储姓名，手机号，座机号
def set_name_phone(folder, _arr1):
    print(_arr1)
    if os.access(folder, os.F_OK):
        with open(folder, 'a+', newline='')as folders:
            writers = csv.writer(folders)
            writers.writerows(_arr1)
            folders.close()
    else:
        with open(folder, 'a+', newline='')as folders:
            writers = csv.writer(folders)
            writers.writerow(['href'])
            writers.writerows(_arr1)
            folders.close()


if __name__ == '__main__':
    print('开始')
    get_url()
