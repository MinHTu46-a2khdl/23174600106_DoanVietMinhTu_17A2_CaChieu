def la_so_nguyen_to(n):
    return n > 1 and all(n % i for i in range(2, n))
def la_so_hoan_hao(n):
    S = sum(i + n//i for i in range(1, int(n**0.5)+1) if n % i == 0)
    return n > 1 and n == S-n
danh_sach = [int(so) for so in input("Nhập danh sách số nguyên dương, cách nhau bởi khoảng trắng: ").split()]
print(f"""
Số nguyên tố trong danh sách: {[so for so in danh_sach if la_so_nguyen_to(so)]}
Số hoàn hảo trong danh sách: {[so for so in danh_sach if la_so_hoan_hao(so)]}""")