# items() -> The items() method returns a view object that displays a list of dictonary`s (key,value) tuple pairs.

# Syntax -> dictionary.items() 

#  items() method doesn`t take any parameters.`




d={
    'name':'Ayush',
    'Enr':"22BT04025",
    'Course':"B.Tech CSE"
}

print(d.items())
print()

for i,j in d.items():
    print(i,j)