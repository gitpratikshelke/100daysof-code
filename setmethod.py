#set methods
#day 32
#union of two sets
s={1,2,3,7,8}
s1={9,8,7,6,1,2,3}
print(s.union(s1))
s.update(s1)
print(s,s1)

city1={"pune","baramati","mumbai"}
city2={"delhi","pune","berlin"}
city3=city1.union(city2)
print(city3)

#intersection of two set
city1={"pune","baramati","mumbai"}
city2={"delhi","pune","berlin"}
city1.intersection_update(city2)
print(city1)

#symmetric diffrence
city1={"pune","baramati","mumbai"}
city2={"delhi","pune","berlin"}
city3=city1.symmetric_difference(city2)
print(city3)

#diffrence
city1={"pune","baramati","mumbai"}
city2={"delhi","pune","berlin"}
city3=city1.difference(city2)
print(city3)

#some inbuilt method

#isdisjoint()           ***o/p in true or false
city1={"pune","baramati","mumbai"}
city2={"delhi","pune","berlin"}
print(city1.isdisjoint(city2))

#issuperset()
city1={"pune","baramati","mumbai"}
city2={"delhi","pune","berlin"}
city3={"kedgaon","urali","loni"}
print(city1.issuperset(city3))

#issubset()
city1={"pune","baramati","mumbai"}
city2={"delhi","pune","berlin"}
city3={"kedgaon","urali","loni"}
print(city1.issubset(city3))

#add()
city1={"pune","baramati","mumbai"}
city1.add("kedgaon")
print(city1)

#remove()
city1={"pune","baramati","mumbai"}
city1.remove("baramati")        #for removing it must be in the main set
print(city1)

#discard()
city1={"pune","baramati","mumbai"}
city1.discard("kedgaon")
print(city1)

#pop()
city1={"pune","baramati","mumbai"}
item=city1.pop()
print(city1)
print(item)

#del()
city1={"pune","baramati","mumbai"}
#del city1
print(city1)

#clear()
city1={"pune","baramati","mumbai"}
city1.clear()
print(city1)


