print("2")
print("a)")
a = 2
while a < 100:
    i = 2
    while i * i <= a:
      if a % i == 0:
        break
      i += 1
    if i * i > a:
      print(a,end = " ")
    a += 1
print("\nb)") 
a = 1
while a**2 < 101:
    print(a**2,end=" ")
    a += 1
print("\nc)")
a = 1
b = 0
while b < 1000:
    print(b, end=" ")
    a, b = b, a + b