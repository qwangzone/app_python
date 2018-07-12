class GouZao:
    b = 0

    def __init__(self, a):
        self.d = 1
        self.b = a

    def wq1(self):
        print("wq1")

    def wq2(self):
        print("wq2")

class Wg:
    def __init__(self,shili):
        self.gouzao = shili

    def print1(self):
        self.gouzao.wq1()

    def print2(self):
        self.gouzao.wq2()


if __name__ == '__main__':
    t1 = GouZao(1)
    t2 = GouZao(2)
    print(t1.b)
    print(t2.d)







