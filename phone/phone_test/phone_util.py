# coding=utf-8
import time
import datetime
import pymongo


# 设置文件生成时间
def set_data_time(st):
    # time_ = time.localtime(time.time())#time_.tm_hour,小时
    data_day = datetime.date.today()
    folder = 'E:\sc\四川%s%s.csv' % (data_day, st)
    return folder


def set_mongo(arr_):
    print()
    mongo = pymongo.MongoClient('localhost:27017')
    http = mongo['http']
    api = http['api']
    api.insert_one(arr_)
