from typing import Iterable, Iterator
from datetime import datetime,timedelta



class Fib():
    def __init__(self):
        print("调用__init__")
        self.a,self.b = 0,1

    def __iter__(self):
        print("调用__iter__")
        return self

    def __next__(self):
        print("调用__next__")
        self.a, self.b = self.b, self.a+self.b
        if self.a>100:
            raise StopIteration
        return self.a


wq = Fib()
print(isinstance(wq,Iterable))
# for i in wq:
#     pass
    #print(i)