# coding=utf-8

import requests
from bs4 import BeautifulSoup
import json


def getIpAddress():
    print()
    ip = "171.221.217.40"
    apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" % ip
    content = requests.get(apiurl)
    html=content.text
    print(html)
    data = json.loads(html)['data']
    code = json.loads(html)['code']
    if code == 0:
        print ("ip:%s from %s%s%s \n" % (data["ip"].encode('utf-8'),data["country"].encode('utf-8'),data["region"].encode('utf-8'),data["city"].encode('utf-8')))
    else:
        print (data.encode('utf-8'))


def get_phone():
    url = 'https://sckyc.atobo.com.cn/'
    url_respone = requests.get(url)
    soup_phone = BeautifulSoup(url_respone.text, 'html.parser')
    # 获取每页的HTML源码字符串
    html_arr = soup_phone.select('html')
    print(html_arr)


if __name__ == '__main__':
    print()
    # get_phone()
    getIpAddress()
