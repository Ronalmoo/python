# IS-A의 관계를 프로그램에서 표현할 때는 상속(inheritance)를 사용한다.
class Computer:
    """
    super class
    """
    def __init__(self, cpu, ram):
        self.CPU = cpu
        self.RAM = ram

    def browse(self):
        print('browse')

    def work(self):
        print('work')


class Laptop(Computer):
    # 멤버 추가
    def __init__(self, cpu, ram, battery):
        super().__init__(cpu, ram)
        self.battery = battery

    # 메서드 추가
    def move(self, to):
        print('move to {}'.format(to))


if __name__ == '__main__':
    lap = Laptop('intel', 16, 'powerful')
    lap.browse()
    lap.work()
    lap.move('office')