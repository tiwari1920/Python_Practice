# Python Progra to calculate GCD using Recursion

def GCD(a, b):
    r = a % b
    if r == 0:
        return b    
    else:
        return GCD(b, r)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print("GCD of", x, "and", y, "is:", GCD(x, y))