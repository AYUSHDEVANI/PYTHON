l=[22,44,66,88,11,33,55,77,99]

# insertion(index,value) for insert number in any position in list
print("Before insertion : ",l)
l.insert(0,10)
print("After insertion : ",l)

print()

# list_name.append(value) function for insert element/otherlist at last in List
# append is copy as it is data you given that
print("Before insert element in end of list : ",l)
l.append(18)
print("After insert element in end of list : ",l)

print()

# list_name.extend(list_name) insert data into your main list from you given list at end of List
print("Before extend : ",l)
n=[10,20,30,40]
l.extend(n)
print("After extend : ",l)