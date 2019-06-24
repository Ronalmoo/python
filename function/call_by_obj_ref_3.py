# 아예 다른 리스트를 메모리 공간에 새로 만든 다음 이를 참조해 리스트를 변경
def func(li):
    li = ['I am your father', 2, 3, 4]
    return li


if __name__ == '__main__':
    li = [1, 2, 3, 4]
    print(li)