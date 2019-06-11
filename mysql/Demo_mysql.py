#!/usr/bin/python3

# import pymysql
#
# # 打开数据库连接
# db = pymysql.connect("localhost","root","root","mysql" )
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
#
# print ("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()


# 创建数据库表
# import pymysql
#
# # 打开数据库连接
# db = pymysql.connect("localhost","testuser","test123","TESTDB" )
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute() 方法执行 SQL，如果表存在则删除
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# # 使用预处理语句创建表
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
#
# cursor.execute(sql)
#
# # 关闭数据库连接
# db.close()


#################

# 导入MySQL驱动:
import mysql.connector
# 注意把password设为你的root口令:
conn = mysql.connector.connect(user='root', password='root', database='test')
cursor = conn.cursor()
# 创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
print(cursor.rowcount)

# 提交事务:
conn.commit()
cursor.close()
# 运行查询:
cursor = conn.cursor()
cursor.execute('select * from user where id = %s', ('1',))
values = cursor.fetchall()
print(values)
# 关闭Cursor和Connection:
print(cursor.close())
conn.close()
