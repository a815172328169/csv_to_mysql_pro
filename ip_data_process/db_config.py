#!/usr/bin/python3
# coding:utf-8

import pymysql

import diy_exceptions

MYSQL_HOST = '127.0.0.1'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_DBNAME = 'only_test'
MYSQL_CHARSET = 'utf8mb4'


def connect_mysql(sql_command):
    try:
        conn = pymysql.connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            db=MYSQL_DBNAME,
            charset=MYSQL_CHARSET
        )
    except Exception as e:
        print(e)
        #'[!]Connect2DB has an error!\n' + str(e)
        raise diy_exceptions.DBConnectError

    try:
        with conn.cursor() as cursor:
            print(sql_command)
            cursor.execute(sql_command)
            result = cursor.fetchall()
            print(result)
    except Exception as e:
        print(e)
        #'[!]fetchall has an error!\n' + str(e)
    finally:
        cursor.close()
        conn.close()
    return result


if __name__ == '__main__':
    pass