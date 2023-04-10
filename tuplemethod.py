#tuple method
#tuple are immutable .but we change tuple indirectly.
players=("virat","rohit","pant","harry")
temp=list(players)
temp.append("pratik")
temp.pop(3)
temp[2]="rahul"
players=tuple(temp)
print(players)


#tuple method
#count method
tuple1=(0,1,2,3,4,3,4,3,3)
res=tuple1.count(3)
print(res)
re=tuple1.index(3)
print(res)
res=tuple1.index(3,4,8)
print(res)
