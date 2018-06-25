# coding=utf-8

import requests
from bs4 import BeautifulSoup
import csv
import os
import time
from phone1 import phone_util
from mysql import pymysql1

# 首页获取地址
one_url = ['https://www.atobo.com.cn/Companys/s-p26-y{}/'.format(str(i)) for i in range(26, 51)]
one_url1 = ['https://www.atobo.com.cn/Companys/s-p26-s568-y{}/'.format(str(i)) for i in range(2, 100)]
# 所有列表
one_title_url = '#setcolor_area > div.product_contextlist.bplist > ul > li'
# 所有列表href
one_href_url = ' div > ul > li.p_name > div > ul > li.pp_name > a.CompanyName'


def get_html_url():
    for var_url in one_url:
        # time.sleep(20)
        page = one_url.index(var_url)+2
        url_html = requests.get(var_url)
        soup = BeautifulSoup(url_html.text, 'html.parser')
        for var_one in soup.select(one_title_url):
            one_href = var_one.select(one_href_url)
            for two_url in one_href:
                arr_ = []
                url_url = two_url.get('href')
                home_url = 'https:%s' % url_url
                data_ = (str(page), home_url)
                arr_.append(data_)
                pymysql1.set_insert(str(page), home_url)
                #存入本地表格
                # set_csv(phone_util.set_data_time('初始网址'), arr_)


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
            writers.writerow(['page', 'http'])
            writers.writerows(_arr1)
            folders.close()


if __name__ == '__main__':
    print('开始运行！！！')
    # get_phone('https://hyb8816.atobo.com.cn/')
    get_html_url()
