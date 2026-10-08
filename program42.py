# Python functional Programming using reduce()

from functools import reduce

marks = [85, 90, 78, 92, 88]
passed_students = list(filter(lambda x: x >= 80, marks))
print("Passed students:", passed_students)

grace_students = list(map(lambda x: x + 5, passed_students))
print("Grace marks added:", grace_students)
total = reduce(lambda x, y: x + y, grace_students)
print("Total marks of passed students after grace:", total)

average = total / len(grace_students)
print("Average marks of passed students after grace:", average)
