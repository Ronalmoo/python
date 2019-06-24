class Account:
    num_acnt = 0

    @classmethod
    def get_num_acnt(cls):
        """
        ds.get_num_acnt() -> integer

        """
        return cls.num_acnt

    def __init__(self, name, money):
        self.user = name
        self.balance = money
        Account.num_acnt += 1

    def deposit(self, money):
        if money < 0:
            return
        self.balance += money

    def withdraw(self, money):
        if money > 0 and money <= self.balance:
            self.balance -= money
            return money
        else:
            return None

    def transfer(self, other, money):
        '''
        obj.transfer(other, money) -> bool
        other: The object to interact with
        money: money the user wants to send
        :return:
        True if the balance is enough to transfer
        False if not
        '''
        mon = self.withdraw(money)
        if mon:
            other.deposit(mon)
            return True
        else:
            return False

    def __str__(self):
        return 'user : {}, balance : {}'.format(self.user, self.balance)


if __name__ == "__main__":
    # 객체 생성
    my_accnt = Account('greg', 5000)
    your_accnt = Account('john', 1000)

    # 생성 확인
    print('object created')
    print(my_accnt)
    print(your_accnt)
    print()

    my_accnt.deposit(500)
    print('deposit')
    print(my_accnt)
    print()

    print('withdraw')
    money = my_accnt.withdraw(1500)
    if money:
        print('withdrawn money : {}'.format(money))
    else:
        print('Not enough to withdraw')
    print()

    print('class member')
    print(Account.num_acnt)
    print()

    print('class method')
    n_acnt = Account.get_num_acnt()
    print('The number of accounts : {}'.format(n_acnt))

    # 메시지 패싱
    print('message passing')
    print(my_accnt)
    print(your_accnt)
    res = my_accnt.transfer(your_accnt, 2000)
    if res:
        print('transfer succeded')
    else:
        print('transfer falied')
    print(my_accnt)
    print(your_accnt)