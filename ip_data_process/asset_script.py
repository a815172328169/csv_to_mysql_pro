#!/usr/bin/python3
# coding:utf-8
import pandas as pd
import ipv4

def read_csv_values(file):
    # 读取csv文件数据
    data = pd.read_csv("./assets.all/"+file, encoding="utf-8")
    data_3 = list(data.values)
    print(data_3)
    print(len(data_3))
    result = []
    for i in data_3:
        if ipv4.checkip(i[0]):
            result.append(i)

    return result

read_csv_values('error.csv')



