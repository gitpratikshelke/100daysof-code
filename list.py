#day 22
#list"list is collection of ordered elements
#list is changeble
marks=[3,5,6,"pratik",True]
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
#in list index start with 0 index


# print(marks[-3])#NEGATIVE
# print(marks[len(marks)-3])#POSITIVE INDEX
# print(marks[5-3])#POSITIVE INDEX
# print(marks[2])#POSITIVE INDEX

# if 7 in marks:
#     print("yes")
# else:
#     print("no")

#same thing apply for string as well
#if "pr" in pratik:
# print("yes")

# print(marks)
# print(marks[:])#to print all element
# print(marks[1:4:2])   #jump indedx

#list comprehension
#list comprehensions are used for creating  new lists from other iterable like list ,tuple,dictionaries,sets
lst=[i*i for i in range(4)]
print(lst)

lst=[i**2 for i in range(11)] 
print(lst)




