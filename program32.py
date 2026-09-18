from abc import ABC,abstractmethod
class Animal(ABC):
    def eat(self):
        None

class Lion(Animal):
    def eat(self):
        print("Lion eat method")
        print("Lion eats meat")

class Elephant(Animal):
    def eat(self):
        print("Elephant Eat Method")
        print("Elephant eats leaves")

e = Elephant()
e.eat()
l = Lion()
l.eat()