# inner 함수 안에서 b와 c를 변경하기

def outer():
    a = 2
    b = 3

    def inner():
        nonlocal a
        a = 100
    inner()

    print('locals in outer : a = {}, b = {}'.format(a, b))


if __name__ == '__main__':
    outer()
