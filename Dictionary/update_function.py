#  update() -> The update() method updates the dictionary e=with the elements from another dictionary object or from an iterable of key/value pairs.

# Syntax -> dict.update(other_dictionary_name)

#  The update() method takes either a dictionary or an iterable objest of key/value pairs(generally tuples).
#  If update() is called without passing parameters, the dictionary remains unchanged.

d={
    'name': 'Ayush',
    'Enr':"22BT04025",
    'Course':"B.Tech CSE"
}

print("Before update : ",d)
print()
a={
    'Surname':'Devani',     # Add a new key and this value.
    'Enr':"25"              # update the value of Enr.
}
d.update(a)
d.update([('x',17),('y',18),('Course','CSE')])      # Update and add to used tuple.
print("After update : ",d)
