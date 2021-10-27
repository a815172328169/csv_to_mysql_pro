import location
import asset_script
import db_config

def write_data():
    citys = location.province_pinyin
    print(citys)
    for city, city_pinyin in citys.items():
        data = asset_script.read_csv_values(city_pinyin+'.csv')
        sql = u"""insert into ziyou_202110(`IP`,`province`) values"""
        for i in range(len(data)):
            if i == len(data) - 1:
                sql += "('%s', '%s');"%(str(data[i][0]), city)
            else:
                sql += "('%s', '%s'),"%(str(data[i][0]), city)
        db_config.connect_mysql(sql)
        db_config.connect_mysql(u"""UPDATE ziyou_202110 set bIP=INET_ATON(IP)""")

