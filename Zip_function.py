# zip function used for list and tuple
# zip is iteret two list at a same time
# lists are same number of elemnet extra element is ignor 

l1=[11,33,55,77,99]
l2=[22,44,66,88,00]

t=len(l1)

for a,b in zip(l1,l2):
    print(a,b)

print()

for c in range(t):
    print(l1[c],l2[c])