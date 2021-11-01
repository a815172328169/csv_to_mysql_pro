import os

from csv_data_process import DataToMysql
import yaml


if __name__ == '__main__':
    with open('config.yaml', 'r', encoding='utf8') as f:
        str_conf = f.read()
    config = yaml.load(str_conf, Loader=yaml.FullLoader)
    file_name_list = os.listdir(config['FILEDIR'])
    task = DataToMysql()

    # # 批量录入文件夹中所有文件
    # i = 1
    # for file_name in file_name_list:
    #     print('{}开始录入'.format(file_name))
    #     data_list = task.get_data(config['FILEDIR']+file_name)
    #     task.data_to_mysql(data_list)
    #     print('{}录入完成'.format(file_name))
    #     if i == len(file_name_list):
    #         print('数据全部录入完毕')
    #     i += 1
    #     time.sleep(5)

    # # 录入当天数据
    # cur_date = time.strftime('%Y%m%d')
    # data_list = task.get_data(config['FILEDIR'] + 'influxbak' + cur_date + '.csv')
    # task.data_to_mysql(data_list)

    # 录入指定文件数据
    file_path = 'C:/Users/ISSUSER/Desktop/data/influxbak20210915.csv'
    data_list = task.get_data(file_path)
    task.data_to_mysql(data_list)