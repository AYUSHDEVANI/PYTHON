print('''
    + ADD
    - SUBTRACT
    * MULTIPLY
    / DIVIDE
 ''')

num1=float(input("Enter the first value : "))
num2=float(input("Enter the Second value : "))
opre=input("Enter the operator (+,-,*,/) : ")

if (opre=="+"):
    print("Sum = ",(num1+num2))

elif(opre=="-"):
    print("SUBTRACT = ",(num1-num2))

elif(opre=="*"):
    print("MULTIPLY = ",(num1*num2))

elif(opre=="/"):
    print("DIVIDE = ",(num1/num1))

else:
    print("Invalid operator")