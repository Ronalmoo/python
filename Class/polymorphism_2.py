# polymorphism_1에서 만든 Animal 클래스를 추상 클래스로 만들자

from abc import *


# 메서드 구현부를 pass로 해 함수 몸체를 비워 두면 eat()메서드는 추상 메서드가 된다.
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def eat(self):
        pass


class Lion(Animal):
    def eat(self):
        print('eat meat')


class Deer(Animal):
    def eat(self):
        print('eat grass')


class Human(Animal):
    def eat(self):
        print('eat meat and grass')


if __name__ == "__main__":
    animals = list()
    animals.append(Lion())
    animals.append(Deer())
    animals.append(Human())

    for animal in animals:
        animal.eat()
