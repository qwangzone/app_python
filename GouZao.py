class GouZao:
    b = 0

    def __init__(self, a):
        self.d = 1
        self.b = a

    def wq1(self):
        print("GouZao wq1")

    def wq2(self):
        print("wq2")

class Wg(GouZao):
    def __init__(self,shili):
        self.gouzao = shili

    def print1(self):
        print("Wg1")

    def print2(self):
        print("Wg2")
    def wq1(self):
        print("Wg wq1")

    def test(self):
        self.wq1()
        super().wq1()


if __name__ == '__main__':
    t1 = GouZao(1)
    t2 = GouZao(2)
    print(t1.b)
    print(t2.b)
    w = Wg(21)
    w.print1()
    w.test()







