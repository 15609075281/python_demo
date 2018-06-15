# coding=utf-8
import requests
from bs4 import BeautifulSoup
import re


# 正则分析
def getReName(html_text):
    re_text = r'<ul>(.*?)</ul>'  # 匹配任意数量的重复，但是在能使整个匹配成功的前提下使用最少的重复。
    print('获取网页中的联系人对应的手机号：')
    re_html = re.findall(re_text, html_text, re.M | re.I | re.S)  # re.M多行匹配re.I对大小写不敏感
    print(re_html)

    for var_html in re_html:
        # print(var_html)
        num = 0
        var_html1 = var_html.replace("<li>", "").replace("</li>", "").replace("<ul>", "").replace("</ul>", "").replace("</a>","").replace(
            '<span style="padding-right: 1em;"></span>', "").replace('<span style="padding-right: 2em;"></span>', "")
        # test_1=re.findall(r'<li>(.*?)</li>',var_html,re.S)
        print('------------------------------------------------------------------------------------------------------')
        # print(var_html1)
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        # 要是没电话，则跳过进入下一个
        number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in number:
            number_list = "电话： "
            number_list = number_list + i
            if number_list in var_html1:
                num = num + 1
        if num == 0:
                break
            # 处理完后调用writePage() 将每个段子写入文件内
        print(var_html1)

# 获取html源码
def getHtml(url):
    print('获取html源码')
    html_url = requests.get(url)
    getReName(html_url.text)


if __name__ == '__main__':
    print('获取网页中的联系人对应的手机号：')
    getHtml('https://sckyc.atobo.com.cn/')
