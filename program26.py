from functools import reduce
def add(x, y):
    return x + y
# Call add() function inside reduce()
result = reduce(add, range(1, 11))
print(result)
