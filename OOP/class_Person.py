class Person:
    """
    Person
    """
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def give_money(self, other, money):
        self.money -= money;
        other.get_money(money)

    def get_money(self, money):
        self.money += money

    def show(self):
        print('{} : {}'.format(self.name, self.money))


if __name__ == '__main__':
    g = Person('greg', 5000)
    j = Person('john', 2000)

    g.show()
    j.show()

    g.give_money(j, 2000)
    print('')


    g.show()
    j.show()
