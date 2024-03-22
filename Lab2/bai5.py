#bai5
a = int(input())
d = a * 120000
print(" tong so tien can tra la",d * 0.8 if a >= 10 else d * 0.9 if a >= 4 else d * 0.95 if a >= 2 else d)