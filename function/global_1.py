# 전역 변수
# 전역 변수(global variable)는 전체 영역에서 접근할 수 있는 변수이다.
# 따라서 함수 안에서도 접근할 수 있어야 한다.

g_var = 10

def func():
    print('g_var = {}'.format(g_var))


if __name__ == 'main':
    func()

