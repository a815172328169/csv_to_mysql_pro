#!/usr/bin/python3
# coding:utf-8

import db_config


def ziyou():
    try:
        sql = u"""
             CREATE TABLE `ziyou_202110` (

            `id` int(10) unsigned NOT NULL AUTO_INCREMENT,

            `bIP` bigint(11) unsigned,

            `IP` varchar(40) DEFAULT NULL,

            `province` varchar(40) DEFAULT NULL,

            PRIMARY KEY (`id`),

            UNIQUE KEY `uni` (`bIP`) USING BTREE,

            KEY `PRO` (`province`) USING BTREE

            ) ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMENT='自有资产'; """
    except Exception as e:
        print(e)
    else:
        result = db_config.connect_mysql(sql)
        return result

if __name__ == '__main__':
    print(ziyou())