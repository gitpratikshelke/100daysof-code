#day 42
#enumerate function help in for loops for indexing

#normal method
marks=[12,56,34,23,57,83,98]
# index=0
# for mark in marks:
#     print(mark)
#     if(index==5):
#         print("pratik","awewsome")
#     index+=1

#using enumerate function
for index, mark in  enumerate(marks ,start=1):              #start indicates the starting of index
    print(mark)
    if(index==5):
        print("pratik","awewsome")
    
