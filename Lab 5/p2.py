stack =[]
while True:
  print("Menu Based Stack Operation : ")
  print("1. Push")
  print("2. Pop")
  print("3. Display")
  print("4. Exit")
  ch=int(input("Enter your choice (1/2/3/4) : "))
  match ch:
    case 1:
      n=int(input("Enter the number to be push : "))
      stack.append(n)
    case 2:
        print("Poped element is ",stack.pop())
    case 3:
      for i in range(len(stack)):
        if stack[i]== None:
          continue
        else:
            print(stack[i],end=" ")
      print()
    case 4:
      print("Exit the program ..")
      exit()
    case _:
      print("Enter valid choice.")
