#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 导入正则的包，这个包系统自带
import re
from  bs4 import BeautifulSoup
import requests
import time
import datetime
import csv

# 默认页
address_url = 'https://www.atobo.com.cn/Companys/s-p26/'
address_url_2 = ['https://www.atobo.com.cn/Companys/s-p26-y{}/'.format(str(i)) for i in range(2, 50)]
address_url_3 = 'https://www.atobo.com.cn/Companys/s-p26-y2/'

anp_url = 'li.card-right'
one_url = '#setcolor_area > div.product_contextlist.bplist > ul > li '
one_url1111 = 'div > ul > li.p_name > div > ul > li.pp_name > a.CompanyName'


# 创建csv文件地址进行数据保存
def get_csv(add_data):
    print()
    try:
        data_time = datetime.date.today()
        csv_url = "F:\sc\sichuan%s.csv" % data_time
        csvFile = open(csv_url, 'w', newline='')
        writer = csv.writer(csvFile)
        writer.writerow(['公司名字', '联系人', '座机', '手机号'])
        writer.writerows(add_data)
    finally:
        csvFile.close()


# 打开单个连接进行数据抓取
def two(arr_two, arr_two1):
    address_arr = []
    for var_two, var_two1 in zip(arr_two, arr_two1):
        time.sleep(3)
        print('第几个：%s' % arr_two.index(var_two))
        print('第几个：%s' % var_two)
        two_url = requests.get(var_two)
        two_soup = BeautifulSoup(two_url.text, 'html.parser')
        content = two_soup.select(anp_url)
        data = (
            var_two1,
            content[2].text,
            content[3].text,
            content[4].text,
        )
        address_arr.append(data)
        get_csv(address_arr)


# 打开每一页获取每页的链接地址
def one():
    arr = []
    arr1 = []
    for one_url_5 in address_url_2:
        print('第几页： %s' % one_url_5)
        time.sleep(20)
        one_url22 = requests.get(one_url_5)
        soup = BeautifulSoup(one_url22.text, 'html.parser')
        for var in soup.select(one_url):
            var_a = var.select(one_url1111)
            for i in var_a:
                arr1.append(i.text)
                arr.append('https:%s' % i.get('href'))
        two(arr, arr1)


# 统计手机号的方法
def count(html):
    # 手机号正则,"1"代表数字1开头，"[3|4|5|7|8]"代表第2位是3/4/5/7/8中任一个，"\d"代表0~9的数字，"{9}"代表按前面的规则取9次
    pattern_mob = re.compile('1[3|4|5|7|8]\d{9}')
    # 打开html文件
    f = open("F:\htmls/phone.html")
    # 用正则匹配html文件中的内容，匹配结果放在变量result中，结果是list形式，如果匹配到两个就这样['13699999999', '17399999999']
    result = pattern_mob.findall(html.text)
    # 返回匹配结果
    return result


# 随便传入一个url，获得html
def get_ur():
    print('get_ur')
    url = 'https://dongxi123.atobo.com.cn/'
    web = requests.get(url)
    soup = BeautifulSoup(web.text, 'html.parser')
    pointed_div = soup.findAll("html")  # 筛选标签为div且属性class为forFlow的源码
    # 将获得的html数据传给count函数，正则获取这个html里面的手机号
    return count(pointed_div[0])  # 主函数


if __name__ == '__main__':
    # 调用count()函数,并打印返回值
    # print(get_ur())
    one()
    # print(get_ur())
