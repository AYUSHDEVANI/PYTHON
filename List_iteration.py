l=[11,22,33,44,55,66]
a=len(l)
for i in range(a):
    print(l[i])


print()
print()

for i in l:
    print(i)

print()
print("Reverse")
for i in range(a-1,-1,-1):
    print(l[i])