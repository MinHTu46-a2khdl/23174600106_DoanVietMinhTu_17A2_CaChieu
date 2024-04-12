s = int(''.join(c for c in input("nhập chuỗi :") if c.isdigit()))
l = all(s% i != 0 for i in range(2, int(s**0.5) + 1)) and s > 1
print(f"{s} {'là' if l else 'không phải'} số nguyên tố.")