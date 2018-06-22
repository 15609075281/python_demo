# coding=utf-8


import requests


def get():
    url = requests.get('https://www.baidu.com/').text
    return url;


if __name__ == '__main__':
    print(get())
