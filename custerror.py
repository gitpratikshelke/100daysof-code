#day38
#in python we can raise custom errors  by adding the raise keyword
#raising  custom error
a=int(input("enter any value betn 5 and 9"))

# if(a<5 or a>9):
#     raise ValueError("value should be betn 5 and 9")

if(a=="quiet"):
    print("sucessfully")
else :
    raise ValueError("value does not exist")