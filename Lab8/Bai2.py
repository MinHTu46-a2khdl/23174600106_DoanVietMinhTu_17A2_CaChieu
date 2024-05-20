def f(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
n = int(input("Nhập số phần tử n: "))
r = int(input("Nhập số phần tử r: "))
print(f"""Số hoán vị p({n}, {r}) = {f(n) // f(n - r)}
"Số tổ hợp c({n}, {r}) = {f(n) // (f(r) * f(n - r))}""")