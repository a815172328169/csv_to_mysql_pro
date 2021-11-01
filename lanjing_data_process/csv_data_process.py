# -*- coding:utf-8 -*-
import pandas as pd
import time
import yaml

from db_connection import Mysql

with open('config.yaml', 'r', encoding='utf8') as f:
    str_conf = f.read()
config = yaml.load(str_conf, Loader=yaml.FullLoader)


class DataToMysql():

    def get_data(self, file_name):
        #  用pandas读取csv
        data = pd.read_csv(file_name)
        data_list = []
        for name, a, available, bk_cloud_id, charset, content_length, error_code, media_type, message, method, \
            node_id, response_code, status, steps, task_duration, task_id, task_type, url in zip(
            data['name'], data['time'], data['available'], data['bk_cloud_id'], data['charset'], data['content_length'],
            data['error_code'],
            data['media_type'], data['message'], data['method'], data['node_id'], data['response_code'], data['status'],
            data['steps'], data['task_duration'],
            data['task_id'], data['task_type'], data['url']):
            str_time = time.localtime(float(str(a)[:-9]))
            c_time = time.strftime('%Y-%m-%d %H:%M:%S', str_time)
            data_list.append([name, c_time, available, bk_cloud_id, charset, content_length, error_code, media_type,
                              message, method, node_id, response_code, status, steps, task_duration, task_id, task_type,
                              url])
        return data_list

    def data_to_mysql(self, data_list):
        mysql = Mysql(
            host=config['HOST'],
            user=config['USER'],
            password=config['PASSWORD'],
            database=config['DATABASE']
        )

        success_data = len(data_list)
        fail_data = 0
        i = 1
        # 数据写入数据库
        for dataList in data_list:
            sql = "INSERT INTO uptimecheck_http_2(name, time, available, bk_cloud_id, charset, content_length, error_code, media_type, message, method, " \
                  "node_id, response_code, status, steps, task_duration, task_id, task_type, url) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s'," \
                  "'%s','%s','%s','%s','%s','%s','%s','%s')" % (
                      dataList[0],
                      dataList[1],
                      dataList[2],
                      dataList[3],
                      dataList[4],
                      dataList[5],
                      dataList[6],
                      dataList[7],
                      dataList[8],
                      dataList[9],
                      dataList[10],
                      dataList[11],
                      dataList[12],
                      dataList[13],
                      dataList[14],
                      dataList[15],
                      dataList[16],
                      dataList[17],
                  )
            res = mysql.add_data(sql)
            if not res:
                success_data -= 1
                fail_data += 1
                print('第{}条数据录入失败'.format(i))
            i += 1
        print('成功录入{}条数据，失败{}条'.format(success_data, fail_data))
