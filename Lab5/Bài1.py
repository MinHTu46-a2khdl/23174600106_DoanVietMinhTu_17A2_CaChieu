def j(b):
    def c(s):
         s = abs(s)
         return c(s // 2) + str(s % 2)  if s > 0 else  ""
    def q(a):
         d = a*2-int(a * 2)
         return str(int(a * 2)) + q(d) if d != 0 else "1"
    b1 = int(b)
    y = c(b1) if b > 0 else "0" if b == 0 else "-"+c(b1)        
    return y if b % 1 == 0 else y +"."+q(b-b1)
print(j(float(input("nhap so thuc:"))))