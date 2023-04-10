#day 23
#------------------------list methods--------------------------------------
l=[1,45,1,3,4,5,9]
# print(l)
# #-----------------append method---at element at last of list-----------
# l.append(7)
# print(l)


# -----------------sort method---------
# l.sort()
# l.sort(reverse=True)#PRINT IN REVERSE ORDER
# print(l)


#---------INDEX METHOD-----------------
print(l.index(1))
print(l.index(9))

#-------------count method*************
print(l.count(1))

#*******************copy element**********
m=l.copy()
m[0]=0
print(l)

#*********insert method**********
l.insert(1,83)
print(l)

#********extend method************
m=[100,200,300]
l.extend(m)
print(l)

#*********concating two list********
k=l+m
print(l)

# *********clear method******
# l.clear()

#******pop method**********
l.pop(0)
print(l)
