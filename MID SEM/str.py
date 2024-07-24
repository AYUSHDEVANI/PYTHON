str="    ayUsh deVani    "

print("upper function : "+ str.upper())

print("lower function : "+str.lower())

print("Remove leading and trailling whitespaces : strip function : " +str.strip())

str="ayush devani  aaaaa"
# Return: The capitalize() function returns a string with the first character in the capital.
print( str.capitalize())

# Return Value: count() method returns an integer that denotes the number of times a substring occurs in a given string. 

print(str.count('a'))
print(str.count('a',0,2))

print()
print("Index function")
print(str.index('d'))
print(str.index('a'))
# print(str.index('a',1,9))
print(str.index('a',1,10))
print(str.index('a',1))
# print(str.index('z'))

print()
print("Casefold method")

str="Ayush Dev@ni $"
print(str.casefold())

print()
print("center method")
# print(str.center(50,'@'))
print(str.center(24,'@'))
print(str.center(10,'@'))

print()
print("find() method")
str="ayUsH dEvAni"
print(str.find('a'))
print(str.find('a',1))
print(str.find('z'))

print()
print("sawpcase() method")

print(str.swapcase())

print()
print("replace() method")

str="ayush devani"
print(str.replace('a',"AA"))

print()
print("join() method")

str='-'
str1="devani"
print(str.join(str1))

print()
print('format() method')

str="ayush {} devani {}"
print(str.format(17,18))
str="ayush {} devani {}".format(1,6)
print(str)
str="ayush {b} devani {a}"
a=88
b="AAAFAFAF"
print(str.format(b=a,a=b))
print(str.format(b=b,a=a))