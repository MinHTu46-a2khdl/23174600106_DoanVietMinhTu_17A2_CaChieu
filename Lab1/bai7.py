# bài seven
a1 = float(input("Nhập hệ số a1: "))
b1 = float(input("Nhập hệ số b1: "))
c1 = float(input("Nhập hệ số c1: "))
a2 = float(input("Nhập hệ số a2: "))
b2 = float(input("Nhập hệ số b2: "))
c2 = float(input("Nhập hệ số c2: "))
print(f"Nghiệm của hệ phương trình là:")
print(f"x = {round((c1 * b2 - c2 * b1) / (a1 * b2 - a2 * b1), 2):.2f}")
print(f"y = {round((a1 * c2 - a2 * c1) / (a1 * b2 - a2 * b1), 2):.2f}")