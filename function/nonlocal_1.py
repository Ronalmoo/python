a = 1


def outer():
    b = 2
    c = 3
    print(a, b, c)

    def inner():
        d = 4
        e = 5
        print(a, b, c, d, e)

    inner()


if __name__ == '__main__':
    outer()