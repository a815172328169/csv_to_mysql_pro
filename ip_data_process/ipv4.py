#!/usr/bin/python3
# coding:utf-8


import IPy

def checkip(address):
    if '/' in address:
        return False
    if ':' in address:
        return False

    try:
        version = IPy.IP(address).version()  #是否为ipv4地址
        ip = IPy.IP(address)
    except:
        return False

    if version != 4 :
        return False
    if ip.iptype() == 'PRIVATE' :     #是否为ipv4内网地址
        return False
    else:
        return True
