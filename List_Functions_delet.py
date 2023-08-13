l=[30,40,55,66,77,88]

# del function for delet element with out show
print("Before delet : ",l)
del l[2]

print("After delet : ",l)

print()

# pop() function delet element with show which element is delete
print("Before pop function : ",l)


print("Deleted element with pop function : ",l.pop(1))
print("After pop operation : ",l)

print()

#  remove() function delet element with pass element in argument 
l.remove(77)
print("Remove function delet element with number : ",l)

print()

# clear() function for delet all elements of List
l.clear()
print("After clear function : ",l)