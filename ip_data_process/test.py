import time

import datetime

a = 1631635564.0
b = time.localtime(a)
c = time.strftime('%Y-%m-%d %H:%M:%S', b)
# print(c)



# lis = ['l09a', 'cas', 'total', 'lx05']
# lis.remove('total')
# print(lis)
#
# lis2 = ['l09a', 'cas', 'lx05']
# if 'total' in lis2:
#     lis2.remove('total')
# print(lis2)
a = time.strftime('%Y%m%d')
print(type(a))