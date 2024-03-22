#bai8
c = float(input("Nhập hệ số góc a1: "))- float(input("Nhập hệ số góc a2: "))
d = float(input("Nhập hệ số tự do b2: ")) - float(input("Nhập hệ số tự do b1: "))
print("vi Tri tuong doi cua 2 duong thang la","trung nhau" if c == d == 0 else " song song " if d != 0 and c == 0 else "cat nhau")