# 함수 안에서 전역 변수의 변경을 시도
g_var = 10

def func():
    g_var = 20
    print('g_var = {} in function'.format(g_var))
    

if __name__ == '__main__':
    func()
    print('g_var = {} in main'.format(g_var))

