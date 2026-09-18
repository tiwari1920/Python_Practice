#Python Program using list and its methods.
l1 = [1, 2, 3, 4, 5]
l2 = [48,"Satyam",95]
l3 = ["c", "c++", "java", "python",]
l4 = [5, 6, 7, 8, 9, 10]
print(l1,type(l1))
print(l2,type(l2))
print(l3,type(l3))
print(l4,type(l4))

#list methods
#indexing
print(l1[0])
print(l2[1])
print(l3[2])
print(l4[3])
print(l3[1:7:2])
print(l4[::2])


#methods
l1.append(6)
print(l1)
l3.remove("c++")
print(l3)
l1.extend(l4)
print(l1)
print(l3.count("python"))
print(l3.index("c"))
print(l4.pop())
print(l4)
l3.sort()
print(l3)
l3.reverse()
print(l3)
l3.remove("python")
print(l3)


#END