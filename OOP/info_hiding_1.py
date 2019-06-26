# 파이썬에서는 완벽한 정보 은닉이 불가능함
# 프로퍼티 기법 혹은 숨기려는 멤버 앞에 언더바(__)를 두 개 붙이는 것으로
# 약간의 은닉(프로그래머의 실수 줄이기 정도)을 제공 한다.

class Account:
    def __init__(self, name, money):
        self.user = name
        self.balance = money

    def get_balance(self):
        return self.balance

    def set_balance(self, money):
        if money < 0:
            return

        self.balance = money


if __name__ == "__main__":
    my_acnt = Account('greg', 5000)
    my_acnt.balance = -3000
    print(my_acnt.get_balance())