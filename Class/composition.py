# IS-A와 다른 객체 관계로 HAS-A가 있음
# HAS-A에는 합성과 통합이 있다.
# 밑의 예는 합성의 예, 이러한 관계를 맺고 있는 객체들은 객체의 생명주기가 같다.


class CPU:
    pass


class RAM:
    pass


# Computer의 객체가 생성될 때 CPU와 RAM 객체가 생성되고 사라질 때 같이 사라진다.
class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()