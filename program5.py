#Python Program using nested if, if-elif-else
#nested if:
x = 15
if x > 10:
    if x < 20:
        print("x is between 10 and 20")
    else:
        print("x is greater than or equal to 20")
else:
    print("x is less than or equal to 10")

#if-elif-else:
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")