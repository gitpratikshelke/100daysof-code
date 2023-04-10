#day 30
 #*****recursion***=recursion is the process of defining something in terms of itself.
 #factorial example
# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(3))
# print(factorial(4))
# print(factorial(5))

#fibonacci sequaence
n=int(input())
def fibno(n):
    if(n<=1):
        return n
    else:
        return fibno(n-1)+fibno(n-2)
print("fibonacci sequence")
#for i in range(n):
print(fibno(n))





   


    

