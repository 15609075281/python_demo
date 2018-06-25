# coding=utf-8

import requests
from bs4 import BeautifulSoup
import re
import csv
import time
import datetime
import os
import pymongo

re_r = '1[3|4|5|7|8]\d{9}'  # 1代表第一个号码为1;;;[3|4|5|7|8]第二位指定为这几个数；；；\d代表0~9，{9}循环9次

one_url = ['https://www.atobo.com.cn/Companys/s-p26-y{}/'.format(str(i)) for i in range(10,50)]

one_title_url = '#setcolor_area > div.product_contextlist.bplist > ul > li'
one_href_url = ' div > ul > li.p_name > div > ul > li.pp_name > a.CompanyName'

name = 'body > div.contextf > div > div > div.cont-r > div:nth-of-type(1) > div > div > ul:nth-of-type(3) > li.card-right'
telephone = 'body > div.contextf > div > div > div.cont-r > div:nth-of-type(1) > div > div > ul:nth-of-type(4) > li.card-right'
phone = 'body > div.contextf > div > div > div.cont-r > div:nth-of-type(1) > div > div > ul:nth-of-type(5) > li.card-right'


def get_html_url():
    print()
    for var_url in one_url:
        time.sleep(100)
        url_html = requests.get(var_url)
        soup = BeautifulSoup(url_html.text, 'html.parser')
        for var_one in soup.select(one_title_url):
            one_href = var_one.select(one_href_url)
            for two_url in one_href:
                url_url = two_url.get('href')
                home_url = 'https:' + url_url
                print(home_url)
                time.sleep(5)
                # # 调用只获得手机号码的方法
                # get_phone(home_url)
                # 调用获得手机号和姓名
                get_name_phone(home_url)


# 获得手机号和姓名
def get_name_phone(url):
    arr_two = []
    two_url = requests.get(url)
    soup = BeautifulSoup(two_url.text, 'html.parser')
    var_name1 = soup.select(name)
    var_telephone1 = soup.select(telephone)
    var_phone1 = soup.select(phone)
    for var_name, var_telephone, var_phone in zip(var_name1,var_telephone1,var_phone1):
        data_two = (
            var_name.text,
            var_telephone.text,
            var_phone.text
        )
        arr_two.append(data_two)
        print(arr_two)
        set_name_phone(set_data_time('name'), arr_two)


# 存储姓名，手机号，座机号
def set_name_phone(folder, _arr1):
    if os.access(folder, os.F_OK):
        with open(folder, 'a+', newline='')as folders:
            writers = csv.writer(folders)
            writers.writerows(_arr1)
            folders.close()
    else:
        with open(folder, 'a+', newline='')as folders:
            writers = csv.writer(folders)
            writers.writerow(['name', 'telephone', 'phone'])
            writers.writerows(_arr1)
            folders.close()


# 获得手机号码
def get_phone(url):
    arr_data = []
    url_html = requests.get(url).text
    re_phone = re.findall(re_r, url_html, re.M | re.S | re.I)
    re_phone = set(re_phone)
    for car_phone in re_phone:
        data_a = (
            car_phone
        )
        arr_data.append(data_a)
    set_csv(set_data_time('phone'), arr_data)


# 设置文件生成时间
def set_data_time(st):
    time_ = time.localtime(time.time())
    data_day = datetime.date.today()
    folder = 'E:\sc\四川%s-%s点%s.csv' % (data_day, time_.tm_hour, st)
    return folder


# 文件存储
def set_csv(folder, _arr1):
    if os.access(folder, os.F_OK):
        with open(folder, 'a+', newline='')as folders:
            writers = csv.writer(folders)
            writers.writerows(_arr1)
            folders.close()
    else:
        with open(folder, 'a+', newline='')as folders:
            writers = csv.writer(folders)
            writers.writerow(['phone'])
            writers.writerows(_arr1)
            folders.close()


if __name__ == '__main__':
    print('开始运行！！！')
    # get_phone('https://hyb8816.atobo.com.cn/')
    get_html_url()
