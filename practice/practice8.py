class unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        print("{0} 유닛이 생성 돼었습니다.".format(name, hp))

    def move(self, movePoint):
        print("{0} 유닛이 {1} 위치로 이동 하였습니다.".format(self.name, movePoint))

    def unitDamage(self, damage):
        self.hp -= damage
        if self.hp <=0 :
            print("{0} 유닛이 {1} 데미지를 입고 사망".format(self.name, damage))
        else :
            print("{0} 유닛이 {1} 데미지를 입음".format(self.name, damage))

class fly:
    def __init__(self, flySpeed):
        self.flySpeed = flySpeed

    def flyMove(self, flyPoint):
        print("{0} 유닛이 {1} 속도로 {2} 지점으로 이동".format(self.name, self.flySpeed, flyPoint))

class unFly:
    def __init__(self, dp):
        self.dp = dp

class flyAttack(unit, fly):
    def __init__(self, name, hp, flySpeed, attackDamage):
        unit.__init__(self, name, hp)
        fly.__init__(self, flySpeed)
        self.attackDamage = attackDamage

class testUnit(flyAttack, unFly):
    def __init__(self, name, hp, flySpeed, attackDamage, dp):
        flyAttack.__init__(self, name, hp, flySpeed, attackDamage)
        unFly.__init__(self, dp)
        print("{0} 이름의 {1} 를 가지고 테스트 유닛이 생성".format(self.name, self.dp))

at = flyAttack("발키리", 100, 8, 200)
at.unitDamage(300)
dummy = testUnit("미이라", 50, 9, 100, 100)
dummy.unitDamage(500)