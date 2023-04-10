#day 38
#finally
#finally code is always exceuted
#finally also executed after the function return
def func1():
    try:
        l=[1,2,3,4]
        i=int(input("enter the index:"))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("i am always exceuted")

x=func1()
print(x)