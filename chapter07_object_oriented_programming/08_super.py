# ===========================================
# 예제 1 : super()를 이용한 부모 생성자 호출
# ===========================================

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

# 건물 유닛
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) 
        # super()를 사용할 때는 self를 전달하지 않는다
        self.location = location

# 서플라이 디폿
supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# =====================================
# 예제 2 : 다중 상속에서 super() 동작
# =====================================

class Unit: 
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__() 
        # MRO(Method Resolution Order) 에 따라
        # 순서상 맨 처음에 상속받는 Flyable의 생성자만 호출된다.
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()
