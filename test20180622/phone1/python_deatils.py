# coding=utf-8

import requests
from bs4 import BeautifulSoup
import csv
import time
import os
import pymongo
import pymysql.cursors
from mysql import pymysql1
from phone1 import phone_util

name = 'body > div.contextf > div > div > div.cont-r > div:nth-of-type(1) > div > div > ul:nth-of-type(3) > li.card-right'
telephone = 'body > div.contextf > div > div > div.cont-r > div:nth-of-type(1) > div > div > ul:nth-of-type(4) > li.card-right'
phone = 'body > div.contextf > div > div > div.cont-r > div:nth-of-type(1) > div > div > ul:nth-of-type(5) > li.card-right'


# 获得手机号和姓名
def get_name_phone(url):
    # arr_two = []
    two_url = requests.get(url)
    soup = BeautifulSoup(two_url.text, 'html.parser')
    var_name1 = soup.select(name)
    var_telephone1 = soup.select(telephone)
    var_phone1 = soup.select(phone)
    for var_name, var_telephone, var_phone in zip(var_name1, var_telephone1, var_phone1):
        data_two = (
            var_name.text,
            var_telephone.text,
            var_phone.text
        )
        # arr_two.append(data_two)
        print('数据源', data_two)
        set_insert(var_name.text, var_telephone.text, var_phone.text)
        # 保存数据到本地表格
        # set_name_phone(phone_util.set_data_time('name'), arr_two)


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


def get_mysql():
    arr_ = pymysql1.get_findall()
    for vv in range(25, len(arr_)):
        page_ = arr_[vv]
        print(arr_.index(page_))
        time.sleep(10)
        get_name_phone(page_[0])


# 插入数据
def set_insert(name, telephone, phone):
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='',
        db='python',
        charset='utf8'
    )
    # 获取游标
    cursor = connect.cursor()
    # 插入语句
    sql = "INSERT INTO phone_name(name,telephone,phone) VALUES ('%s','%s','%s')"
    data = (name, telephone, phone)
    cursor.execute(sql % data)
    connect.commit()
    print('成功插入', cursor.rowcount, '条数据')
    cursor.close()
    connect.close()


if __name__ == '__main__':
    print()
    get_mysql()
