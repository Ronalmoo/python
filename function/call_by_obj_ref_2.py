# 참조한 리스트에 접근해 변경을 시도
def func(li):
    li[0] = 'I am your father!'


if __name__ == '__main__':
    li = [1, 2, 3, 4]
    func(li)
    print(li)