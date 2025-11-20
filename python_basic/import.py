import time
print(time.localtime())

import time as t
print(t.localtime())
print(t.time())

from time import localtime,time   #仅仅只用time和localtime两种功能\
print(time())
print(localtime())

from time import*    #使用所有功能
print(time())
print(localtime())
print(gmtime())  #格林威治时间 gmtime