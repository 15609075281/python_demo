# coding=utf-8

import requests
import re
from phone1 import phone_home

# 获得手机号码
re_r = '1[3|4|5|7|8]\d{9}'  # 1代表第一个号码为1;;;[3|4|5|7|8]第二位指定为这几个数；；；\d代表0~9，{9}循环9次


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
    print(phone_home.set_data_time('phone'), arr_data)


if __name__ == '__main__':
    print()
    str=input('输入链接地址:')
    print(str)
    get_phone(str)
