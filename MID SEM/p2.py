a=5  #0101
b=6  #0110
print((a&b))

print(a|b)

print(a^b)

print("a 1 right shift : " , a>>1)
print("a 1 left shift : ", a<<1)
print("b 3 right shift : ",b>>3)
print("b 2 right shift : ",b>>2)

print()
a=5
b=15
print((a<10 and b>10))
print(a and b)
print(a>10 and b<10)

print(a>10 or b>10)

print(a<10 or b<10)

print(a>10 or b<10)

print(not(a>10 or b<10))

print(not(a))
print(not())