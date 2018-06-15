# coding=utf-8
import csv


# 从字典写入csv文件
def set_Csv2():
    dic = {'张三': 123, '李四': 456, '王二娃': 789}
    csvFile3 = open('D:\csv\csvFile4.csv', 'w', newline='')
    writer2 = csv.writer(csvFile3)
    writer2.writerow(['id', 'username', 'password', 'address'])
    writer2.writerows([[333, 333, 333, 333]])
    csvFile3.close()


if __name__ == '__main__':
    print()
    set_Csv2()
