# List is an ordered sequence of items.
# It is one of the most used datatype in Python and is very flexible.
# List is a mutable datatype.
# []

l=[10,2,3,5,'Ayush']

print(l)
print(type(l))
l[2]=20
print(l)

# nested list

l=[1,2,3,[4,5,6]]
print(l[3][2])


# mixed list

l=[2,3,"Hello",[3,4,5]]
print(l[-2])

# list slicing
# list[start index:end index:increment/decrement]

l=[1,2,3,4,5,6]

print(l[1:4])
print(l[-1::-1])
print(len(l))