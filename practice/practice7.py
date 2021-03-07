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

class fly(unit):
    def __init__(self, name, hp, flySpeed):
        unit.__init__(self, name, hp)
        self.flySpeed = flySpeed

    def flyMove(self, flyPoint):
        print("{0} 유닛이 {1} 속도로 {2} 지점으로 이동".format(self.name, self.flySpeed, flyPoint))

class flyAttack(fly):
    def __init__(self, name, hp, flySpeed, attackDamage):
        fly.__init__(self, name, hp, flySpeed)
        self.attackDamage = attackDamage


marine = unit("마린",50)
marine.move("50:210")
marine.unitDamage(50)
wraith = fly("레이스", 60, 5)
wraith.move("20:100")

at = flyAttack("발키리", 100, 8, 200)
        