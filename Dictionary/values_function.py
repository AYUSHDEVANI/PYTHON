# valyes() -> The values() method returns a view object that displays a list of all the values in the dictionary.

# Syntax -> dict.values()

#  values() does not take any parameters.

d={
    'name' : 'Ayush',
    'Enr': '22BT04025',
    'Course':'B.tech CSE'
}

print(d.values())
print()

for i in d.values():
    print(i)