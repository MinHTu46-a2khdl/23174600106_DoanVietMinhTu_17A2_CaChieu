n = int(input("Nhập số lượng số Fibonacci: "))
fibonacci = [0, 1]
[fibonacci.append(fibonacci[-2] + fibonacci[-1]) for _ in range(n - 2)]
so_nguyen_to = [m for m in range(2, 100) if all(m % i != 0 for i in range(2, int(m**0.5) + 1))]

print(f"""
Danh sách các số nguyên tố nhỏ hơn 100: {so_nguyen_to}
Danh sách {n} số Fibonacci đầu tiên: {fibonacci}""")