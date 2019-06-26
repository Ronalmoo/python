class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def init_from_string(cls, string):
        """

        string format: '<name>_<age>'

        """
        name, age = string.split('_')
        return cls(name, int(age))


if __name__ == "__main__":
    p = Person.init_from_string('greg_30') # 클래스 메서드로 대체 생성자를 생성
    p1 = Person('greg', 30)
    print(p.name)
    print(p.age)
    print(p1.name)
    print(p1.age)