# Python functional Programming using filter(), map()

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
squared_numbers = list(map(lambda x: x ** 2, even_numbers))
doubled_numbers = list(map(lambda x: x * 2, squared_numbers))
print("Even numbers:", even_numbers)
print("Squared numbers:", squared_numbers)
print("Doubled numbers:", doubled_numbers)