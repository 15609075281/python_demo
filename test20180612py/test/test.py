import pymongo

client = pymongo.MongoClient('localhost', 27017)  # 第一个元素数据库连接地址，第二个元素端口号
student = client['student']  # 创建表
login = student['login']  # 创建登录表

# path = 'C:/Users/Administrator/Desktop/cs.txt'
# with open(path, 'r')as f:
#     lins = f.readlines()
#     for index, line in enumerate(lins):
#         data = {
#             'index': index,
#             'line': line,
#             'words': len(line.split())
#         }
#         login.insert_one(data)

for item in login.find({'words': {'$lt': 1}}):
    print(item['words'])


