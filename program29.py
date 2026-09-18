class A:
    def display(self):
        print("Parent class A")
        print("Display Method")

class B(A):
    def display(self):
        print("Child class B")
        print("Display Method")

obj1 = B()
obj1.display()