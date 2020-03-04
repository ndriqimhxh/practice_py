class Pointx:
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point1 = Pointx()
point1.draw()
point1.x = 10
point1.y = 20
print(point1.x)

#Constructors
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Person:
    def __init__(self, name):            #initaliazer constructor
        self.name = name
    def talk(self):
        print(f"Hi, I am {self.name}")
john = Person("John Smith")
print(john.name)
john.talk()