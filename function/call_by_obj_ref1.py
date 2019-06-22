def change_value(x, value):
    x = value
    print('x : {} in change_value'.format(x))


if __name__ == '__main__':
    x = 10
    change_value(x, 20)
    print('x : {} in main'.format(x))