ds = list(map(int, input("Nhập dãy số nguyên: ").split()))
a = all(ds[i] - ds[i - 1] == ds[1] - ds[0] for i in range(2, len(ds)))
print(f"Dãy số {ds} {'là' if a else 'không phải'} cấp số cộng.")