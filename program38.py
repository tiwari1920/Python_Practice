# Python Program to print finding exponents x power y using Recursion

def exp(x,y):
    if y == 0:
        return 1
    else:
        return x * exp(x, y - 1)

a = int(input("Enter the base number (x): "))
b = int(input("Enter the exponent (y): "))
result = exp(a, b)
print(f"{a} raised to the power of {b} is: {result}")