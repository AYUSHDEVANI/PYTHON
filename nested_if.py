num=int(input("Enter the number : "))

if(num>0):
    if(num<=10):
        print("The number bitween 1-10")
    elif(num>10 & num<=100):
        print("The number bitween 11-100")
    else:
        print("The number is greater than 100")
elif(num<0):
    print("The number is negative")
else:
    print("The number is Zero")