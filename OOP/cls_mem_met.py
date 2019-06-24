class A:
    c_mem = 10


    @classmethod
    def cls_f(cls):
        print(cls.c_mem)

    def __init__(self, num):
        self.i_mem = num

    def ins_f(self):
        print(self.i_mem)


if __name__ == "__main__":
    print(A.c_mem)
    A.cls_f()

    a = A(20)
    print(a.c_mem)
    a.cls_f()
