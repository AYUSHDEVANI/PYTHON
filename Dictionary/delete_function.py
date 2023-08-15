# del ->  The del keyword can be used to in-palce delete the key that is present in the dictionary in Python. 

# Syntax -> del dict[key]

d={
    'name':"Ayush",
    'Enr':"22BT04025",
    'Course':"B.Tech CSE"
}

print("Before delete : ",d)
del d['Enr']

print()
print("After delete : ",d)

#  pop() -> The pop() can be used to delete a key and its value inplace. The advantage over using del is that it provides the mechanism to print desired value if tried to remove a non-existing dict. Second it also returns the value of the key that is being removed in addition to performing a simple delete operation. Demonstarting key-valye pair deletion using pop().

A={
    'Collage':'GSFC UNIVERSITY',
    'City':'Vadodara',

}
print()
print("Before delete : ",A)

print("Deleted value : ", A.pop('City'))

print("After delete : ",A)