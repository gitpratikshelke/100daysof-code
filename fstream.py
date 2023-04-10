#day 28
#string format is used to format to string
letter = "hey my name is {} and I am from {}"
country="India"
name="pratik"
print(letter.format(name,country))


#using fstream
print(f"hey my name is{name} and i am from {country}")
print(f" we use fstream like -this hey my name is{{name}} and i am from {{country}}")


price=49.09999
txt=f"for only {price:.2f} dollars!"
print(txt)