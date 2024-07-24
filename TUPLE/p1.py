# A tuple is created by placing all the items(elements) inside parentheses '()' , seperated by commas ",". The parentheses are optional.and
# A tuple can have any number of items and they may be of different types (integer, float, list, string, etc).

# A tuple is a collection which is ordered and immutable.
# iterating through tuple is faster than list  

t=(40,20,30,10,50,10)
print(t[1])
print(t[3])

print()
print("print with for in loop : ")
for a in t:
    print(a)

print("Length : ",len(t))
print("Type : ",type(t))
print()

print("Print tuple with range : ")
for i in range(len(t)):
    print("Index ",i," on value ",t[i])

print("Minimum value in tuple : ",min(t))
print("Maximum value in tuple : ",max(t))

print("Count method : ",t.count(10))
print("Index method : ",t.index(50))
print('Sum method : ',sum(t))
print('Sum method : ',sum(t,50))


# print()
# print()
# print()
# a=None
# print(a)
# print(type(a))
# print(bool(a))