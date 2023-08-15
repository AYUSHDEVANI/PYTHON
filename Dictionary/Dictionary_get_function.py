# get() -> The get() method returns the value of the specified key in teh dictionary.
        # syntax -> dict.get(key[,value])
                    # key-> key to be searched i the dictionary
                    # value(optional)-> Value to be returned if the 'key' is not found. The default value is none.

d={
    'name' : 'Ayush',
    'surname': 'Devani',
    'Enr' : '22BT04025'

}
# a=d.get('aa',[100])
print(d.get('Enr'))
print(d.get('AA',100))