#  In pyhton a nested dictionary is a dictionary inside a dictionary. it`s a collection of dictionaries into one single dictionary.SyntaxError


A ={
    'b':{
            'x':17,
            'y':18
        },

    'c':{
            'name':'Ayush',
            'Enr':'22BT04025',
            
        }
}

print(A)
print()
print(A['b'])
print()
print(A['b']['y'])

print()
print(A['c'])
print()
print(A['c']['name'])
print()

for i,j in A.items():
    print(i,j)

print()
for i,j in A.items():
    print(A[i].values())
    