#bai1
print(1)
#a
a = int(input("nhap so nguyên duong :"))
print("a)",sum(i for i in range(1, a+1 if a > 0 else int(input("số vừa nhập không đúng,vui lòng nhập lại :")) + 1)))
#b

a = int(input("nhap so nguyên duong :"))
print("b)",sum(1/i for i in range(1, a+1 if a > 0 else int(input("số vừa nhập không đúng,vui lòng nhập lại :")) + 1)))
#c
a = int(input("nhap so nguyên duong :"))
print("c)",sum(1/(i*2)**0.5 for i in range(1, a+1 if a > 0 else int(input("số vừa nhập không đúng,vui lòng nhập lại :")) + 1)))
#d
a = int(input("nhap so nguyên duong :"))
print("d)",sum((-1/i)**(i+1) for i in range(1, a +1if a> 0 else int(input("số vừa nhập không đúng,vui lòng nhập lại :")) + 1))) 