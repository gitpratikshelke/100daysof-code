#day 21
'''def average(a,b):
    print("the average is",(a+b)/2)
average(4,8)

4 types of arguments
1.default 
2.keywoed
3.variable length
4.required


def average(a=9,b=1):
    print("the average is",(a+b)/2)
average(4)#default argument

def name(fname,mname="xyz",lname="pqr"):
    print("hello",fname,mname,lname)
name("ijk")#first name is default argument

average(b=32,a=12)#argument mattrers not the order of arguments///this is keyword argument


#required arguments:the name says all'''

#variable length 
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
        print("average is",sum/len(numbers))
average(6,7,1)
