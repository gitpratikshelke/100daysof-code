#day45

def welcome():
    print("hey you are welcome")

welcome()

print(__name__)
if __name__==" __main__":   #this is common pattern used in python scripts to determine whether the script is run directly or being imported as a module into another script
    welcome()