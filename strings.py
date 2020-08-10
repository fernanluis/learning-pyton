myStr = "Hello world"

dir(myStr)

# print(dir(myStr))

myStr = "Hello World"
# print(dir(myStr)) comentamos para evitar que se ejecute.
print(myStr.upper())
print(myStr.lower())
print(myStr.swapcase())
print(myStr.capitalize())
print(myStr.replace("hello", "bye"))
print(myStr.replace("hello", "bye").upper())
print(myStr.count("l"))
print(myStr.count("o"))
print(myStr.count(" "))
print(myStr.startswith("hola"))
print(myStr.startswith("hello"))
print(myStr.startswith("h"))
print(myStr.startswith("hel"))
print(myStr.endswith("world"))


myStr = "hello world"
print(myStr.split())

print(myStr.find('o'))

print(myStr.find(" "))

print(len(myStr))

print(myStr.index('e'))

# print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[4])

myStr = "Fernando"

print("My name is " + myStr)

#print(f"My name is {myStr}")
print("My name is {0}".format(myStr))
