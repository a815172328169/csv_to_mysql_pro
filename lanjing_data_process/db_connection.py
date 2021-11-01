import pymysql


class Mysql:
    def __init__(self, host, user, password, database):
        try:
            self.conn = pymysql.connect(host=host, user=user, password=password, database=database)  # 连接数据库
        except Exception as e:
            print(e, '数据库连接失败')
        else:
            print('数据库连接成功')
            self.cur = self.conn.cursor()

    '''创建表'''
    def create_table(self, sql):
        try:
            self.cur.execute(sql)
        except Exception as e:
            print(e, '表创建失败')
        else:
            print('表创建成功')

    '''添加数据'''
    def add_data(self, sql):
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
            return True
        else:
            self.conn.rollback()
            return False
