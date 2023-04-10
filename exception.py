#day36
#exception handling
a=input("enter the number..")
print(f"multiplication table of {a} is:")
try:
    for i in range (1,11):
        print(f"{{int a}} X {i}={int(a)*i}")
except ValueError:
    print("invalid input")
except IndexError:
    print("number is invalid:")

# print("some imp lines of codes")
# print("end of programm")