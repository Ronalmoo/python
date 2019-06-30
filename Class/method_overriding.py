# method overriding이란, 상속 관계에 있는 다양한 클래스의 객체에서 같은 이름의 메서드를 호출할 때,
# 각 객체가 서로 다르게 구현된 메서드를 호출함으로써 서로 다른 행동, 기능, 결과를 가져오는 것을 말한다.
# 같은 이름의 메서드를 호출해도 호출한 객체에 따라 다른 결과를 내는 것을 '다형성'이라고 한다.
class CarOwner:
    def __init__(self, name):
        self.name = name

    def concentrate(self):
        print('{} can not do anything else'.format(self.name))


class Car:
    def __init__(self, owner_name):
        self.owner = CarOwner(owner_name)

    def drive(self):
        self.owner.concentrate()
        print('{} is driving now.'.format(self.owner.name))


class SelfDrivingCar(Car):
    def drive(self):
        print('Car is driving by itself')


if __name__ == '__main__':
    car = Car('Greg')
    car.drive()
    print('')

    s_car = SelfDrivingCar('john')
    s_car.drive()
