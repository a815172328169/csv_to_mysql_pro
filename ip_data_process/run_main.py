#!/usr/bin/python3
# coding:utf-8
import db_config
import db_process
import asset_script
import db_write

def main():

    service_result = db_process.ziyou()
    try:
        db_write.write_data()

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()