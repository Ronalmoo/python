# 프로퍼티를 이용하면 멤버에 접근하는 것 처럼 보이지만
# 사실은 메서드를 호출한다.

class Account:
    def __init__(self, name, money):
        self.user = name
        # 인스턴스 멤버 선언이 아니라 balance.setter 메서드를 호출
        self.balance = money

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, money):
        if money < 0 :
            return

        # 실제 인스턴트 멤버 선언이 일어나는 부분
        self._balance = money


if __name__ == "__main__":
    my_acnt = Account('greg', 5000)
    my_acnt.balance = -3000

    print(my_acnt.balance)