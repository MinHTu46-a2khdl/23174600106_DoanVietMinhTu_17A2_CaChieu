a = input("nhập chuỗi 1 :")
a2 = input("nhập chuỗi 2 :")
print('-'.join(f"{a[i]}-{a2[i]}" for i  in range(min(len(a), len(a2)))))