#tuple
#it is the ordered  collection of items .tuples are unchangeble 
tup =(1,2,3,4,56,7,342)
print(type(tup),tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(len(tup))


if 342 in tup:
    print("yes 342 is present in tuple")

#new tuple 
tup2=tup[1:4]
print(tup2)