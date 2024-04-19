mang = [int(so) for so in input("Nhập mảng số nguyên dương, cách nhau bởi khoảng trắng: ").split()]
print(f"""
Tổng số chẵn: {sum(so for so in mang if so % 2 == 0)}
Tổng số lẻ: {sum(so for so in mang if so % 2 != 0)}""")


