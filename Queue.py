l=[]

while True:
    c=int(input('''
            1. Push Eelement.
            2. Pop First Element.
            3. Front Element.
            4. Last Element.
            5. Dispaly Queue.
            6. Exit
                
            Enter your option : '''))

    if c==1:
        n=input("Enter value : ")
        l.append(n)
        print("Queue is : ",l)

    elif c==2:
        if len(l)==0:
            print("Queue is Empty.")

        else:
            print("Poped element is : ",l[0])
            del l[0]
            print("Queue is : ",l)

    elif c==3:
        if len(l)==0:
            print("Queue is Empty.")
        else:
            print("First Element is : ",l[0])

    elif c==4:
        if len(l)==0:
            print("Queue is Empty.")
        else:
            print("Last Element is : ",l[-1])
    elif c==5:
        if len(l)==0:
            print("Queue is Empty.")
        else:
            print("Queue : ",l)
    elif c==6:
        print("Exit Succefully..")
        break;

    else:
        print("Invalid option....")

