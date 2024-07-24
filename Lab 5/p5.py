n1=int(input("Enter the size of first matrix : "))
matrix1=[]

print("Enter the elements of first matrix : ")
for i in range(n1):
    temp=[]
    for j in range(n1):
        x = int(input("Enter the element of Matrix[{}][{}]: ".format(i, j)))
        temp.append(x)
    matrix1.append(temp)

n2=int(input("Enter the size of second matrix : "))
matrix2=[]


print("Enter the elements of second matrix : ")
for i in range(n2):
        temp=[]
        for j in range(n2):
            x = int(input("Enter the element of Matrix[{}][{}]: ".format(i, j)))
            temp.append(x)
        matrix2.append(temp)

if (len(matrix1[0]) != len(matrix2)):
    print("Invalid criteria")
    exit()
else:
    result=[]
    for i in range(n1):
        temp=[]
        for j in range(len(matrix2[0])):
            sum=0
            for k in range(len(matrix2)):
                sum +=matrix1[i][k]*matrix2[k][j]
            temp.append(sum)
        result.append(temp)


for i in result:
    print(i)