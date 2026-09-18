def add_10(x):
    x += 10
    return x
print('Values before applying map()')
for i in range(1, 51):
    print(i, end=" ")
# Call add_10() function inside map()
values = list(map(add_10, range(1, 51)))
print('\nValues after applying map()')
print(values)
