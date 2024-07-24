l=[1,2,3,4]
l.append(101010)
print(l)

l2=[5,6,7]
l.extend(l2)
l2.extend(l)
print(l)
print(l2)

print()

l=[1,2,3,4,5,6,7,3,9]
l.remove(3)
print(l)
l.pop(5)
print(l)
l.pop()
print(l)
l.pop()
print(l)


print()

l=[9,8,7,6,5,4,3,2,1]
del l[2]
print(l)

# del l
# print(l)

l.clear()
print(l)
print()

l=[1,2,3,4,5,6,7,8,9]
print(l)
print(l[len(l)::-1])