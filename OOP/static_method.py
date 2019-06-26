# 정적 메서드는 인자로 클래스나 객체를 받지 않는다.
# 함수의 정의만 클래스 A의 네임스페이스에 있을 뿐 일반 함수와 같으며,
# 전역 함수를 대체하기에 가장 알맞다.

class A:
    @staticmethod
    def f():
        print('static method')

    @classmethod
    def g(cls):  # 클래스 메서드는  첫 번째 인자로 클래스 A를 받는다.
        print(cls.__name__)


if __name__ == "__main__":
    a = A()
    a.f() # 정적 메서드
    a.g() # 클래스 메서드