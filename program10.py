#Defining our own module fact_module.py
fact = 1
def factorial(n):
    for i in range(1, n + 1):
        fact = fact * i
    print("The factorial of", n, "is", fact)
