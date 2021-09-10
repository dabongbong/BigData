#상속과 다형성

class Human():
    def walk(self):
        print("걷는다")
    def eat(self):
        print("먹는다")
    def wave(self):
        print("손을 흔든다")

person1 = Human()
person2 = Human()

person1.walk()
person1.eat()
person1.wave()
person2.wave()
person2.eat()
person2.walk()

