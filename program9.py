#Python Program to print multiplication tables in a given range.
a = int(input("Enter the starting number: "))
b = int(input("Enter the ending number: "))
print("Multiplication tables from", a, "to", b)
for i in range(a, b + 1):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
print("Multiplication tables printed successfully.")
print("Thank you for using the program.")