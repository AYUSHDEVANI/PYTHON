l=[11,22,33,44,11,11,'a','z','s','a']
print(l)

print("Count 11 : ",l.count(11))
print("Count a : ",l.count('a'))

print()

n=[11,22,33,44,11,11]
print("list : ",n)
print("Max number in list : ",max(n))

p=["abc","xyz","pqr","efg"]
print("List : ",p)
print("Max alphabet in list : ",max(p))

print()
print("list : ",n)
print("Minimun number in list : ",min(n))
print("List : ",p)
print("Minimun alphabet in list : ",min(p))


print()
n.sort()
print("After sort : ",n)
print()
print("List : ",l)
l.reverse()
print("Reverse list : ",l)

print()
print("List : ",l)
print("Index of 11 : ",l.index(11))
print("Index of 22 : ",l.index(22))
print("Index of 11 after index 4 : ",l.index(11,5))