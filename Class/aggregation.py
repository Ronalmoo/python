# HAS-A의 관계 중 통합을 나타내는 예
# 생명주기를 함께 하지 않는 상대적으로 약한 관계


class Gun:
    def __init__(self, kind):
        self.kind = kind

    def bang(self):
        print('bang bang!')


class Police:
    def __init__(self):
        self.gun = None

    def acquire_gun(self, gun):
        self.gun = gun

    def release_gun(self):
        gun = self.gun
        self.gun = None
        return gun

    def shoot(self):
        if self.gun:
            self.gun.bang()
        else:
            print('Unable to shoot')


if __name__ == '__main__':
    p1 = Police()
    print('p1 shoots')
    p1.shoot()
    print('')

    # p1은 아직 총을 소유하지 않음
    revolver = Gun('Revolver')
    p1.acquire_gun(revolver)
    print('p1 shoots again')
    p1.shoot()
    print('')

    revolver = p1.release_gun()
    print('p1 shoots again')
    p1.shoot()