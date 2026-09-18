class Shape:
    def draw(self):
        print("Parent Class draw method")

class Rectangle(Shape):
    def draw(self):
        print("Child Class draw method")
        print("Drawing Rectangle")

class Circle(Shape):
    def draw(self):
        print("Child circle class draw method")
        print("Drawing Circle")

s = Shape()
s.draw()
r = Rectangle()
r.draw()
c = Circle()
c.draw()