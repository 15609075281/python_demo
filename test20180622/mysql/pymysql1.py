# coding=utf-8

import pymysql
import pymysql.cursors


#
# # 创建数据库表
# connect = pymysql.Connect(
#         host='localhost',
#         port=3306,
#         user='root',
#         passwd='',
#         db='python',
#         charset='utf8'
#     )
#     # 获取游标
# cursor = connect.cursor()


# 插入数据
def set_insert( page, api):
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
    print()
    # 插入语句
    sql = "INSERT INTO python(page,api) VALUES ('%s','%s')"
    data = (page, api)
    print('数据库:', page, api)
    cursor.execute(sql % data)
    connect.commit()
    print('成功插入', cursor.rowcount, '条数据')
    cursor.close()
    connect.close()


# 更新数据
def set_updata():
    print()
    sql = "UPDATE python SET name='%s' WHERE id=%s"
    data = ('二号数据', 0)
    cursor.execute(sql % data)
    connect.commit()
    print('更新了', cursor.rowcount, '条数据')
    cursor.close()
    connect.close()


# 查询数据
def get_findall():
    print()
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
    sql = "select api from python"
    cursor.execute(sql)
    api_arr = cursor.fetchall()
    return api_arr
    # print('共查出', cursor.rowcount, '条数据')
    cursor.close()
    connect.close()


# 删除数据
def delete_():
    print()
    sql = "DELETE FROM python WHERE id =%s "
    data = (0,)
    cursor.execute(sql % data)
    connect.commit()
    print('成功删除', cursor.rowcount, '条数据')
    cursor.close()
    connect.close()


# # 事务处理
# sql_1 = "UPDATE trade SET saving = saving + 1000 WHERE account = '18012345678' "
# sql_2 = "UPDATE trade SET expend = expend + 1000 WHERE account = '18012345678' "
# sql_3 = "UPDATE trade SET income = income + 2000 WHERE account = '18012345678' "
#
# try:
#     cursor.execute(sql_1)  # 储蓄增加1000
#     cursor.execute(sql_2)  # 支出增加1000
#     cursor.execute(sql_3)  # 收入增加2000
# except Exception as e:
#     connect.rollback()  # 事务回滚
#     print('事务处理失败', e)
# else:
#     connect.commit()  # 事务提交
#     print('事务处理成功', cursor.rowcount)


if __name__ == '__main__':
    print()
    get_findall()
