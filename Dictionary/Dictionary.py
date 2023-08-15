# Dictionary is an unordered collection of key-value pairs.
# In python, dictionary are defined within curly braces {} with each item being a pair in the form key:value

d={
    'name':'Ayush',
    'Enr':"22BT04025",
     1:"AY"
    
    }
print(d)
print(type(d))
print(d['name'])
print(d['Enr'])
print(d[1])

for i in d:
    print(i,d[i])