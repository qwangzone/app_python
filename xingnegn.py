from datetime import datetime
import time
def runtime(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        endtime = datetime.now().timestamp()
        diff = endtime-statime
        print("%s()运行时间："%func.__name__+str(diff))
        return res
    statime = datetime.now().timestamp()
    return wrapper

def add():
    sum = 10
    time.sleep(1)
    return sum
@runtime
def wtest1():
    k =1
    while k<add():# 每次循环都会调用add函数，调用sum次add函数，sum越大，调用的次数越多
        k = k+1
    print(k)

@runtime
def wtest2():
    k =1
    num = add()  #调用一次add()函数
    while k<num:
        k = k+1
    print(k)


if __name__ == '__main__':
   # wtest1()
    wtest2()
