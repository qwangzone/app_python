from datetime import datetime
import time,sys,os


def log(func):
    def wrapper(*args,**kwargs):
        print("call %s():" %func.__name__)
        return func(*args,**kwargs)
    return wrapper

def runtime(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        end_time = datetime.now().timestamp()
        print("函数执行时间为：%d"%(end_time-start_time))
        return res

    start_time = datetime.now().timestamp()
    #print(start_time)
    return wrapper

@runtime
@log
def now(x,y):
  #time.sleep()
  return x+y
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.now())
print(now(3,4))

import os,sys
a = "/app_python"
print(os.path.isdir(a))
print(os.listdir(a))
for i in os.listdir(a):
    if os.path.isdir(i):
        print(i+ "是个目录")
    else:
        print(i+ "是个文件")
