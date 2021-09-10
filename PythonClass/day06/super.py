class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print("먹는다")
    def walk(self):
        print("걷는다")
    def greet(self):
        print("{}이/가 인사한다.".format((self.name)))

class Human(Animal):
    def __init__(self, name, hand):
        super().__init__(name)
        self.hand = hand
    def wave(self):
        print("{}을 흔들면서".format(self.hand), end = " ")
    def greet(self):
        self.wave()                 # self 는 자기자신
        super().greet()             # super() 는 부모

# person = Human("길동")
person = Human("길동","오른손")
# person.greet()


class Car():
    def __init__(self, name):
        self.name = name
    def run(self):
        print("차가 달린다!")

class Truck(Car):
    def __init__(self, name, capa):
        super().__init__(name)
        self.capa = capa


    def load(self):
        print("짐을 싣습니다.")

