myStr ="Hello World"

# properties and methods of the variable
print(dir(myStr))

print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.strip())

print(myStr.replace("Hello", "Bye"))

print(myStr.count("l"))

print (myStr.split())


print ("a,b,c,d".split(","))

print(myStr.find("o"))

print(myStr.index("o"))

print(myStr.isnumeric())

print(myStr.isalpha())

print(myStr[4]) # character in position 4
print(myStr[-1]) # last character


print("My name is "+ myStr) # concatenation of string - operator +
print(f"My name is {myStr}") # using a variable in a text - command f

print ("My name is {0}".format(myStr))

