from collections import Counter
chuoi = input()
k = [char for char in chuoi if not char.isalnum()]
print(f"""
Ký tự đặc biệt trong chuỗi: {k}
Số lần xuất hiện của các ký tự đặc biệt là: {Counter(k)}
Tỷ lệ xuất hiện ký tự đặc biệt là: {len(k) * 100 / len(chuoi):.2f}%
""")