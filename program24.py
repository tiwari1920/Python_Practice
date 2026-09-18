d1 = {"Emp Id": 8001, "ename": "Tiwari", "job": "manager"}
d2 = {"Emp Id": (101, 102, 103), "ename": ['A', 'B', 'c']}
print(d1)
print(d2)
# Print dict values using for loop
for k, v in d1.items():
    print(k, v)
for k, v in d2.items():
    print(k, v)
# Adding new element to dictionary
d1['salary'] = 10000
print(d1)
# Deleting element from dictionary
del d1["job"]
print(d1)
