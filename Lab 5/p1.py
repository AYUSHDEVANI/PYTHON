while True:
  print("Menu - Based Calculator : ")
  print("1. Add")
  print("2. Subtract")
  print("3. Multiply")
  print("4. Divide")
  print("5. Exit")
  ch=int(input("Enter your choise (1/2/3/4/5) : "))
  match ch:
    case 1:
      n1=int(input("Enter first number : "))
      n2=int(input("Enter second number : "))
      n3=n1+n2
      print("Result : ",n3)
    #   break
    case 2:
      n1=int(input("Enter first number : "))
      n2=int(input("Enter second number : "))
      n3=n1-n2
      print("Result : ",n3)
    #   break
    case 3:
      n1=int(input("Enter first number : "))
      n2=int(input("Enter second number : "))
      n3=n1*n2
      print("Result : ",n3)
    #   break
    case 4:
      n1=int(input("Enter first number : "))
      n2=int(input("Enter second number : "))
      n3=n1/n2
      print("Result : ",n3)
    #   break

    case 5:
      print("Exit from the Calculator ...")
      exit()

    case _:
      print("Enter valid choise..")
