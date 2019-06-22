# 지역 변수 안에서 전역 변수값 변경하기
g_var = 10


def func():
    global g_var
    g_var = 20


if __name__ == '__main__':
    print('g_var : {} before'.format(g_var))
    func()
    print('g_var : {} after'.format(g_var))