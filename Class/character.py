# 클래스 계층을 설계할 때 고려해야할 사항
# 1. 공통 부분을 기본 클래스로 묶는다. 이렇게 하면 코드를 재사용할 수 있다.
# 2. 부모가 추상 클래스인 경우를 제외하고, 파생 클래스에서 기본 클래스의 여러 메서드를 오버라이딩한다면 파생 클래스는 만들지 않는 것이 좋다.

from abc import *

# 추상 클래스로 만든다.


class Character(metaclass=ABCMeta):
    def __init__(self, name, hp, power):
        self.name = name
        self.HP = hp
        self.power = power

    @abstractmethod
    def attack(self, other, attack_kind):
        pass

    def get_damage(self, power, attack_kind):
        pass

    def __str__(self):
        return '{} : {}'.format(self.name, self.HP)


class Player(Character):
    def __init__(self, name='player', hp=100, power=10, *attack_kinds):
        super().__init__(name, hp, power)

        # 추가된 인스턴스 멤버
        self.skills = []
        for attack_kind in attack_kinds:
            self.skills.append(attack_kind)

    # 재정의된 attack() 메서드
    # 반드시 재정의되어야 한다.
    def attack(self, other, attack_kind):
        if attack_kind in self.skills:
            other.get_damage(self.power, attack_kind)

    # 재정의된 get_damage() 메서드
    # 반드시 재정의되어야 한다.
    def get_damage(self, power, attack_kind):
        """

        :param power:
        :param attack_kind: 만약 공격 종류가 player 기술 중 하나라면 반감
        :return:
        """
        if attack_kind in self.skills:
            self.HP -= (power // 2)
        else:
            self.HP -= power

