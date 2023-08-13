name = "Ayush Patel !!!!"

print("Length of string : ",len(name))

print("Orignal name :",name)

print("Convert into upper case : ",name.upper())

print("Conver into lower case :",name.lower())

print("Remove trailing character : ",name.rstrip("!"))

print("Replace : ",name.replace("Patel","Devani"))

print("Split : ",name.split(" "))

Heading="introduction of Python.."

print("Capatalization : ",Heading.capitalize())

print("Center : ",Heading.center(50))
print("Lenght without center method : ",len(Heading))
print("Lenght with center method : ",len(Heading.center(50)))

print("Count : ",Heading.count("python"))

print("End with .. : ",Heading.endswith("..."))

print("Find 'of' : ",Heading.find("of"))

print("Index 'of' : ",Heading.index("of"))

str="AyushDevani18"

print("check A-Z, a-z, 0-9 : ",str.isalnum())

str2="AyushDevani"
print("Check A-Z, a-z : ",str2.isalpha())

str3="ayush devani"
print("Check lower case : ",str3.islower())

str4="Ayush Devani"
print("Check printable : ",str4.isprintable())