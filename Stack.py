l=[]

while True:
    c=int(input('''
        1. Push Element
        2. Pop Element
        3. Peek Element
        4. Display Stack
        5. Exit
        Pleas enter your option : '''))
    if(c==1):
        n=input("Enter the value : ")
        l.append(n)
        print("Stack : ",l)
    elif c==2:
        if len(l)==0:
            print("Stack is Empty.")
        else:

            p=l.pop()
            print("Deleted element is : ",p)
            print("Stack : ",l)

    elif c==3:
        if len(l)==0:
            print("Stack is Empty.")
        else:
            k=l[-1]
            print("Last element is : ",k)

    elif c==4:
        if len(l)==0:
            print("Stack is Empty.")
        else:
            print("Stack is : ",l)

    elif c==5:
        print()
        print("Exit succefully.")
        break;

    else:
        print("Please enter valid option...")