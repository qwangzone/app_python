from datetime import datetime
import time


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
def now(x,y):
  time.sleep(3)
  return x+y

print(now(3,4))